from django import template
from django.contrib.auth.models import Group
from mainapp.utils import *

register = template.Library()

@register.filter
def isotime(datestring):
    datestring = str(datestring)
    return datestring.replace("T"," ")

@register.filter(name='as_ti')
def get_nama(user):
	try:
		pengguna = Pengguna.objects.get(user=user)
		result = pengguna.nama
	except Exception as e:
		result = user.username

	return result

@register.simple_tag
def check_user_role(request):
	userLogin = UserLogin(request)
	result = userLogin.role

	return result

@register.filter(name='has_group')
def has_group(user, group_name):
	group = Group.objects.get(name=group_name)
	return True if group in user.groups.all() else False

@register.filter(name='as_title')
def as_title(param):
	title = param.replace("_", " ")
	title = title.title()
	return title

@register.simple_tag
def get_object_value(object, attr):
	result = getattr(object, attr)
	if result is None:
		result = '-'
	return result
