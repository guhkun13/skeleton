import os
import socket

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'au=5ciq2l$gsft%o9lz&necik#yd5d#7-nmkw9w@#s0z&6ek_1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
import os

DIR = os.path.dirname(os.path.abspath(__file__))
paths = DIR.split('/')
env_dir = paths[3]

hostname = socket.gethostname()
root_url = env_dir
remote_hostname = 'host-ws1-dev-CYBER2-10-12-200-31'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'mainapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'skeleton.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'layouts')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'skeleton.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

if root_url == 'devliatlog':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
        'billing': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
           'HOST': '10.12.200.100',
           'NAME': 'dev',
           'USER': 'billing_btns',
           'PASSWORD': 'billing_btns_dev',
           'PORT': '5432',
        },
        'switching': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
           'HOST': '10.12.200.100',
           'NAME': 'dev',
           'USER': 'switching_btns',
           'PASSWORD': 'sesuatubtns',
           'PORT': '5432',
       }
    }
elif root_url == 'liatlog':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
        'billing': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
           'HOST': '10.12.100.100',
           'NAME': 'prod',
           'USER': 'billing_btns',
           'PASSWORD': 'billing_btns_prod',
           'PORT': '5432',
        },
        'switching': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
           'HOST': '10.12.100.100',
           'NAME': 'prod',
           'USER': 'switching_btns',
           'PASSWORD': 'switching_btns_prod',
           'PORT': '5432',
       }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
        'billing': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
           'HOST': '127.0.0.1',
           'PORT': '5432',
           'NAME': 'btnsportal',
           'USER': 'postgres',
           'PASSWORD': 'postgres',           
        },
        'switching': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
           'HOST': '127.0.0.1',
           'PORT': '5432',
           'NAME': 'switching',
           'USER': 'switching_btns',
           'PASSWORD': 'switching_btns',
       }
    }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
USE_THOUSAND_SEPARATOR = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_PATH = os.path.join(BASE_DIR, '../assets')
STATIC_ROOT = os.path.join(BASE_DIR, '../static')

STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = '/index/'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'

if hostname == remote_hostname:
    STATIC_URL = '/'+root_url+'/static/'
    LOGIN_REDIRECT_URL = '/skeleton/index/'
    LOGIN_URL = '/'+root_url+'/login/'
    LOGOUT_URL = '/'+root_url+'/logout/'

STATICFILES_DIRS = (STATIC_PATH,)

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'msg-info',
    messages.INFO: 'msg-info',
    messages.SUCCESS: 'msg-success',
    messages.WARNING: 'msg-warning',
    messages.ERROR: 'msg-error',
}
