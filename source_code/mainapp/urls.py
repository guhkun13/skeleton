# from django.conf.urls import *
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from skeleton.settings import root_url

from . import views
app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name="index"),
    path(root_url+'/', views.index, name="index"),
    path(root_url+'/index/', views.index, name='index'),
    path(root_url+'/accounts/login/', views.login, name='login'),
    path(root_url+'/login/', views.login, name='login'),
    path(root_url+'/logout/', LogoutView.as_view(next_page='/'+root_url+'/login/'), name='logout'),
    path(root_url+'/dashboard/', views.dashboard, name="dashboard"),
    path(root_url+'/ajax/datatables/<str:model>', views.AjaxDatatables.as_view(), name='ajax_datatables'),

    # custom
    path(root_url+'/log_general/', views.log_general, name="log_general"),
    path(root_url+'/trx/', views.trx, name="trx"),

]
