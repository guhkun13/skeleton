# from django.conf.urls import *
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views
app_name = 'mainapp'


urlpatterns = [
    path('', views.index, name="index"),
    path('skeleton/', views.index, name="index"),
    path('skeleton/index/', views.index, name='index'),
    path('skeleton/accounts/login/', views.login, name='login'),
    path('skeleton/login/', views.login, name='login'),
    path('skeleton/logout/', LogoutView.as_view(next_page='/skeleton/login/'), name='logout'),
    path('skeleton/dashboard/', views.dashboard, name="dashboard"),
    path('skeleton/delete_biller/<pk>/', views.delete_biller, name="delete_biller"),
]
