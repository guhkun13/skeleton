import json
import socket
from pprint import pprint

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
    return render(request, html, context)

class AjaxDatatables(View):

    def post(self, request, model):
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
        datas = modelClass.get_all_data()
        records_total = datas.count()
        records_filtered = records_total

        if search:
            datas = modelClass.filter_search(search)

        datas = filter_specific_column(datas, datatables)
        datas = datas.order_by(order_col_name)

        records_total = datas.count()
        records_filtered = records_total

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
    model_name = 'log_inquiry'
    context = {
        'app':model_name,
        'selectedModel':'log_inquiry'
    }

    html = "mainapp/"+model_name+"/index.html"
    return render(request, html, context)

@login_required()
def log_general(request):
    app_name = 'log_general'
    model_selected = request.GET.get('model_name')
    list_model_log = ['log_inquiry', 'log_payment', 'log_reversal']

    if not model_selected in list_model_log:
        model_selected = 'log_inquiry'

    context = {
        'app':app_name,
        'modelSelected': model_selected
    }

    html = "mainapp/log/index.html"
    return render(request, html, context)

@login_required()
def trx(request):
    model_name = 'trx'
    context = {
        'app':model_name,
        'modelSelected':'trx'
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
def create_biller(request):
    _DEBUG	     = 10
    _INFO	     = 20
    _SUCCESS     = 25
    _WARNING	 = 30
    _ERROR	     = 40

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
