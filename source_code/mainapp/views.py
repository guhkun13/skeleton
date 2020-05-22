from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout, get_user
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from switching.models import Mapping
from .utils import *

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

import socket
from datetime import datetime

@login_required()
def dashboard(request):
    filter_tipe_biller = ''

    context = {}
    datas = Mapping.objects.using('switching').all()

    if (request.GET.get('form_filter')):
        filter_tipe_biller = request.GET.get('filter_tipe_biller')
        if (not filter_tipe_biller==''):
            datas = datas.filter(tipe_biller=filter_tipe_biller)

    if (request.POST):
        tipe_biller     = request.POST.get('tipe_biller')
        url_inquiry     = request.POST.get('url_inquiry')
        url_payment     = request.POST.get('url_payment')
        url_reversal    = request.POST.get('url_reversal')

        if tipe_biller == 'H2H':
            if url_inquiry == "" or url_payment == "" or url_reversal == "" :
                url = 'mainapp/dashboard.html'
                msg_false = 'URL INQ/PAY/REV tidak boleh kosong untuk Tipe Biller H2H'

                context = {'msg_false': msg_false}
                return render(request, url, context)
        try:
            billerBaru = Mapping.objects.using('switching').create(
                kode_biller     = request.POST.get('kode'),
                nama_biller     = request.POST.get('nama'),
                tipe_biller     = request.POST.get('tipe_biller'),
                tipe_bayar      = request.POST.get('tipe_bayar'),
                url_inquiry     = request.POST.get('url_inquiry'),
                url_payment     = request.POST.get('url_payment'),
                url_reversal    = request.POST.get('url_reversal'),
                creator         = request.POST.get('creator'),
                catatan         = request.POST.get('catatan'),
                created_at      = datetime.now()
            )

            return HttpResponseRedirect(reverse('mainapp:dashboard'))
        except Exception as e:
            raise e

    context['datas'] = datas
    context['filter_tipe_biller'] = filter_tipe_biller

    html = 'mainapp/dashboard.html'
    return render(request, html, context)

@login_required()
def delete_biller(request, pk):
    try:
        instance = Mapping.objects.using('switching').get(kode_biller=pk)
        instance.delete()
    except Exception as e:
        raise e

    return HttpResponseRedirect(reverse('mainapp:dashboard'))
