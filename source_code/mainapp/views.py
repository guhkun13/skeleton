from distutils.log import Log
import json
import socket
from pprint import pprint
from xmlrpc.client import DateTime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout, get_user
from django.contrib.auth.decorators import permission_required, user_passes_test, login_required
from django.contrib import auth, messages

from django.views.generic import DetailView, View

from .utils import *


from mainapp.ajax_class.utils import *
from django.core.serializers.json import DjangoJSONEncoder
from skeleton.settings import root_url

from datetime import datetime

_DEBUG	     = 10
_INFO	     = 20
_SUCCESS     = 25
_WARNING	 = 30
_ERROR	     = 40

_LOG_INQ = 'log_inquiry'
_LOG_PAY = 'log_payment'
_LOG_REV = 'log_reversal'
_TRX     = 'trx'

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('mainapp:login'))
    elif request.user.is_authenticated:
        return HttpResponseRedirect(reverse('mainapp:dashboard'))

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('mainapp:index'))
    elif request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']
        user_login = auth.authenticate(username=username, password=password)

        if not user_login is None :
            print ("user is not None, go to index")
            auth_login(request, user_login)
            return HttpResponseRedirect(reverse('mainapp:index'))
        else:
            url = 'registration/login.html'
            msg_false = 'Your username or password wrong'

            context = {'msg_false': msg_false}
            return render(request, url, context)
    else:
        url = 'registration/login.html'
        return render(request, url)

@login_required()
def dashboard(request):
    html = 'mainapp/dashboard.html'
    data = get_data_dashboard()

    context = {
        'app' : 'dashboard',
        'data' : data,        
    }

    # print(data)
    return render(request, html, context)

class AjaxDatatables(View):

    def post(self, request, model):
        print('AjaxDatatables_post')        
        datas = self._process(request, model)
        return HttpResponse(json.dumps(datas, cls=DjangoJSONEncoder), content_type='application/json')

    def _process(self, request, model):
        modelClass = get_model_class(model)

        datatables = request.POST
        params = process_params(datatables)

        draw = params['draw']
        start = params['start']
        length = params['length']
        search = params['search']
        order_col_name = params['order_col_name']

        # datas = get_data_by_model(model)
        year = request.POST.get('year_selected') or None
        month = request.POST.get('month_selected') or None

        print ('year/month = {}/{}'.format(year, month))

        datas = modelClass.get_all_data(year=year, month=month)
        records_total = datas.count()
        records_filtered = records_total

        print('[before filter] records_total = ' + str(records_total))

        if search:
            print('do search')
            datas = modelClass.filter_search(search)

        datas = filter_specific_column(datas, datatables)
        datas = datas.order_by(order_col_name)

        records_total = datas.count()
        records_filtered = records_total

        print('[after filter] records_total = ' + str(records_total))

        object_list = process_paginator(datas, start, length)
        data = modelClass.generate_data(object_list)

        return {
        	'draw': draw,
        	'recordsTotal': records_total,
        	'recordsFiltered': records_filtered,
        	'data': data,
        }


# *********** CUSTOM VIEWS HERE ************* #
@login_required()
def log_inquiry(request):
    model_name = _LOG_INQ
    context = {
        'app':model_name,
        'selectedModel':_LOG_INQ
    }

    html = "mainapp/"+model_name+"/index.html"
    return render(request, html, context)

import calendar


@login_required()
def log_general(request):
    app_name = 'log_general'
    available_months = []

    available_months.append({"id": 0, "name":"ALL"})
    idxm = 1
    for month in calendar.month_name[1:]:
      available_months.append({"id": idxm, "name":month})
      idxm += 1
    
    # print (available_months)

    model_selected = request.GET.get('model_name')

    year_selected = request.GET.get('year_selected')
    month_selected = request.GET.get('month_selected')

    print ('yearSel / monthSel = {}/{}'.format(year_selected, month_selected))

    list_model_log = [_LOG_INQ, _LOG_PAY, _LOG_REV]

    available_years = []
    list_years = None
    if not model_selected or model_selected == '':
        model_selected = _LOG_INQ
    
    list_years = get_years_from_records(model_selected)
    
    # if year_selected:
    #   print ('year_selected true = ' + str(year_fselected))
    #   list_years = get_years_from_records(model_selected)

    # print('list_years', list_years)
    
    if list_years:
      for item in list_years:
        available_years.append(str(item['year']))
    
    c_year = datetime.now().year
    c_month = datetime.now().month

    if not month_selected:
      month_selected = c_month

    if not available_years:
      year_selected = str(c_year)
      available_years = [str(c_year)]
    else:
      print ('else available_years', available_years)
      print ('year_selected = ', year_selected)

      # tahun sudah di-sort DESC. 
      # ambil year yang terbaru jika kosong atau tahun yang dipilih tidak tersedia di log
      if not year_selected or str(year_selected) not in available_years:
        year_selected = available_years[0]
        
    context = {
        'app':app_name,
        'model_selected': model_selected,
        'year_selected': year_selected,
        'month_selected': int(month_selected),
        'available_years': available_years,
        'available_months': available_months,
    }

    # print('context')
    print(context)

    html = "mainapp/log/index.html"
    return render(request, html, context)


@login_required()
def trx(request):
    model_name = 'trx'

    year_selected = request.GET.get('year_selected')

    available_years = []
    list_years = get_years_from_records(model_name)

    print('list_years', list_years)
    if list_years:
      for item in list_years:
        available_years.append(str(item['year']))
    
    c_year = datetime.now().year

    if not available_years:
      year_selected = str(c_year)
      available_years = [str(c_year)]
    else:
      print ('else available_years', available_years)
      print ('year_selected = ', year_selected)

      if not year_selected or str(year_selected) not in available_years:
        year_selected = available_years[0]

    context = {
        'app':model_name,
        'modelSelected':'trx',
        'yearSelected': year_selected,
        'available_years': available_years,
    }

    html = "mainapp/"+model_name+"/index.html"
    return render(request, html, context)

from django.db.models import Count
from django.db.models.functions import ExtractMonth, ExtractYear

def get_years_from_records(model_name):
  print('get_years_from_records '+ model_name)
  qs = None
  if model_name == _LOG_INQ:    
    qs = LogInquiry.objects.using('billing').values(year=ExtractYear('ts'))
  elif model_name == _LOG_PAY:    
    qs = LogPayment.objects.using('billing').values(year=ExtractYear('ts'))
  elif model_name == _LOG_REV:    
    qs = LogReversal.objects.using('billing').values(year=ExtractYear('ts'))
  elif model_name == _TRX:
    qs = Payment.objects.using('billing').values(year=ExtractYear('ts'))

  qs = qs.annotate(count_year=Count('year')).order_by('-year');
    
  return qs



@login_required()
def rekon(request):
    model_name = 'rekon'
    context = {
        'app':model_name,
        'modelSelected':'rekon'
    }

    html = "mainapp/"+model_name+"/index.html"
    return render(request, html, context)

@login_required()
def biller(request):
    model_name = 'mapping_biller'
    context = {
        'root_url':root_url,
        'app':model_name,
        'modelSelected':'mapping_biller'
    }

    html = "mainapp/"+model_name+"/index.html"
    return render(request, html, context)

@login_required()
def create_or_update_biller(request):

    if (request.POST):
        tipe_biller     = request.POST.get('tipe_biller')
        url_inquiry     = request.POST.get('url_inquiry')
        url_payment     = request.POST.get('url_payment')
        url_reversal    = request.POST.get('url_reversal')

        if tipe_biller == 'H2H':
            if url_inquiry == "" or url_payment == "" or url_reversal == "" :
                msg = 'URL INQ/PAY/REV tidak boleh kosong untuk Tipe Biller H2H'

                messages.add_message(request, _ERROR, msg)
                return HttpResponseRedirect(reverse('mainapp:biller'))
        if request.POST.get('update_biller'):
            # update existing biller
            try:

                billerExist = Mapping.objects.using('switching').get(kode_biller=request.POST.get('kode'))
                billerExist.kode_biller     = request.POST.get('kode')
                billerExist.nama_biller     = request.POST.get('nama')
                billerExist.tipe_biller     = request.POST.get('tipe_biller')
                billerExist.tipe_bayar      = request.POST.get('tipe_bayar')
                billerExist.url_inquiry     = request.POST.get('url_inquiry')
                billerExist.url_payment     = request.POST.get('url_payment')
                billerExist.url_reversal    = request.POST.get('url_reversal')
                billerExist.catatan         = request.POST.get('catatan')
                billerExist.updated_at      = datetime.now()
                billerExist.save()

                msg = "Existing biller:" + billerExist.kode_biller +"/" + billerExist.nama_biller +" has been updated! :D"
                messages.add_message(request, _INFO, msg)
                return HttpResponseRedirect(reverse('mainapp:biller'))
            except Exception as e:
                raise e
        else:
            try:
                billerBaru = Mapping.objects.using('switching').create(
                    kode_biller     = request.POST.get('kode'),
                    nama_biller     = request.POST.get('nama'),
                    tipe_biller     = request.POST.get('tipe_biller'),
                    tipe_bayar      = request.POST.get('tipe_bayar'),
                    url_inquiry     = request.POST.get('url_inquiry'),
                    url_payment     = request.POST.get('url_payment'),
                    url_reversal    = request.POST.get('url_reversal'),
                    catatan         = request.POST.get('catatan'),
                    creator         = request.POST.get('creator'),
                    created_at      = datetime.now()
                )

                msg = "New biller has been born! :D"
                messages.add_message(request, _INFO, msg)
                return HttpResponseRedirect(reverse('mainapp:biller'))
            except Exception as e:
                raise e
    else:
        return HttpResponseRedirect(reverse('mainapp:biller'))

@login_required()
def delete_biller(request, pk):
    print("pk = ", pk)
    try:
        instance = Mapping.objects.using('switching').get(kode_biller=pk)
        instance.delete()
    except Exception as e:
        raise e

    return HttpResponseRedirect(reverse('mainapp:biller'))

@login_required()
def edit_biller(request, pk):
    model_name = 'mapping_biller';
    print("pk = ", pk)
    try:
        instance = Mapping.objects.using('switching').get(kode_biller=pk)
        # print(instance)

        if instance.url_inquiry is None:
           instance.url_inquiry = '' 
        
        if instance.url_payment is None:
               instance.url_payment = '' 
        
        if instance.url_reversal is None:
               instance.url_reversal = '' 

        if instance.creator is None:
               instance.creator = '' 
        
        if instance.catatan is None:
               instance.catatan = '' 


        context = {
            'instance':instance,
            'app':model_name,
            'modelSelected':'mapping_biller'
        }

        html = "mainapp/"+model_name+"/edit_biller.html"
        return render(request, html, context)

    except Exception as e:
        raise e

    return HttpResponseRedirect(reverse('mainapp:biller'))


from csv import *
import csv
# guhkun
@login_required()
def upload_csv_biller(request):
    print ("request.POST => ", request.POST)
    print ("request.FILES => ", request.FILES)

    upload_file = request.FILES['upload_file']
    print("upload_file => ", upload_file)

    data_set = upload_file.read().decode('UTF-8').splitlines()
    print("data_set => ", data_set)

    cnt_berhasil = 0
    msg = ""
    msg_gagal = ""
    reader = csv.reader(data_set)

    firstline = True
    for row in reader:
        
        if firstline:    #skip first line
            firstline = False
            continue
        
        try:
            get_object_or_404(Mapping.objects.using('switching'), kode_biller=row[0])
            msg_gagal = 'Failed biller [' + row[0] + '] already existed'
            messages.add_message(request, _WARNING, msg_gagal)
        except Exception as e:
            try:
                new_biller = Mapping()
                new_biller.kode_biller  = row[0]
                new_biller.nama_biller  = row[1]
                new_biller.tipe_biller  = row[2]
                new_biller.tipe_bayar   = row[3]
                new_biller.url_inquiry  = row[4]
                new_biller.url_payment  = row[5]
                new_biller.url_reversal = row[6]
                new_biller.catatan      = row[7]                
                new_biller.creator      = row[8]
                new_biller.created_at   = datetime.now()
                new_biller.save(using='switching')

                cnt_berhasil+=1

                msg_berhasil = 'Success create biller [' + str(row[0])
            except Exception as e:
                msg_gagal = 'Failed create biller [' + row[0] + ']. Error: ' + str(e)
                messages.add_message(request, _ERROR, msg_gagal)

    msg_berhasil = 'Success create ' + str(cnt_berhasil) + ' biller'
    messages.add_message(request, _INFO, msg_berhasil)


    return HttpResponseRedirect(reverse('mainapp:biller'))
