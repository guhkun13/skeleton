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
    path(root_url+'/ajax/datatables/<str:model>/', views.AjaxDatatables.as_view(), name='ajax_datatables'),
    path(root_url+'/ajax/datatables/<str:model>/<year>/', views.AjaxDatatables.as_view(), name='ajax_datatables'),
    path(root_url+'/ajax/datatables/<str:model>/<year>/<month>/', views.AjaxDatatables.as_view(), name='ajax_datatables'),

    # custom
    path(root_url+'/log_general/', views.log_general, name="log_general"),
    path(root_url+'/trx/', views.trx, name="trx"),
    path(root_url+'/rekon/', views.rekon, name="rekon"),
    path(root_url+'/biller/', views.biller, name="biller"),
    path(root_url+'/create_biller/', views.create_or_update_biller, name="create_biller"),
    path(root_url+'/upload_csv_biller/', views.upload_csv_biller, name="upload_csv_biller"),
    path(root_url+'/delete_biller/<str:pk>', views.delete_biller, name="delete_biller"),
    path(root_url+'/edit_biller/<str:pk>', views.edit_biller, name="edit_biller"),

]
