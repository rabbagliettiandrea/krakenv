# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from datetime import timedelta
from django.utils.functional import SimpleLazyObject
import os


DEBUG = True
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SECRET_KEY = 'i5+_bdfc7co*^!5)w-25#rib97pz^bqoxyt3_a^$r8c58@gvd2'
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'krakenv',
    'krakenv.apps.account_system',
]
MIDDLEWARE_CLASSES = [
    'krakenv.middleware.TentacleDispatcherMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware'
]
ROOT_URLCONF = 'krakenv.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'krakenv', 'templates')],
        'OPTIONS': {
            'loaders': [
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.filesystem.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'krakenv.context_processors.get__settings',
                'krakenv.context_processors.get__datetime_now',
                'krakenv.context_processors.get__user_is_logged'
            ],
        },
    },
]
WSGI_APPLICATION = 'wsgi.application'
DATABASES = {
    'default':     {
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'NAME':     'krakenv',
        'USER':     'djangouser',
        'PASSWORD': 'djangouser',
        'HOST':     '127.0.0.1',
        'PORT':     '5432'
    }
}
DATABASE_ROUTERS = ['krakenv.db.routers.KrakenvRouter']
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
]
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'krakenv', 'static')
]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': False
        },
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True
        },
        'backend': {
            'handlers': ['console', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True
        },
        '': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True
        }
    }
}
CACHE_EXPIRE_TIME = timedelta(days=7).total_seconds()
CACHE_EXPIRE_TIME_RENDERS = timedelta(days=1).total_seconds()
SESSION_COOKIE_AGE = timedelta(weeks=4).total_seconds()
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'session'
REDIS_SERVERS = {
    # Cache
    'default': 'redis://127.0.0.1:6379/0',
    'misc': 'redis://127.0.0.1:6379/1',
    'session': 'redis://127.0.0.1:6379/2',
    'staticfiles': 'redis://127.0.0.1:6379/3',
    'magento_pourich': 'redis://127.0.0.1:6379/4',
    'magento_spesafacile': 'redis://127.0.0.1:6379/5',
    # Direct
    'celery-task': 'redis://127.0.0.1:6379/6',
    'celery-result': 'redis://127.0.0.1:6379/7'
}
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'TIMEOUT': CACHE_EXPIRE_TIME,
        'LOCATION': SimpleLazyObject(lambda: REDIS_SERVERS['default']),
    },
    'misc': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'TIMEOUT': CACHE_EXPIRE_TIME,
        'LOCATION': SimpleLazyObject(lambda: REDIS_SERVERS['misc']),
    },
    'session': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'TIMEOUT': SESSION_COOKIE_AGE,
        'LOCATION': SimpleLazyObject(lambda: REDIS_SERVERS['session']),
    },
    'staticfiles': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'TIMEOUT': CACHE_EXPIRE_TIME,
        'LOCATION': SimpleLazyObject(lambda: REDIS_SERVERS['staticfiles']),
    },
    'magento_pourich': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'TIMEOUT': CACHE_EXPIRE_TIME,
        'LOCATION': SimpleLazyObject(lambda: REDIS_SERVERS['magento_pourich']),
        'OPTIONS': {
            'SERIALIZER_CLASS': 'redis_cache.serializers.JSONSerializer'
        },
        'KEY_FUNCTION': lambda key, key_prefix, version: key
    },
    'magento_spesafacile': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'TIMEOUT': CACHE_EXPIRE_TIME,
        'LOCATION': SimpleLazyObject(lambda: REDIS_SERVERS['magento_spesafacile']),
        'OPTIONS': {
            'SERIALIZER_CLASS': 'redis_cache.serializers.JSONSerializer'
        },
        'KEY_FUNCTION': lambda key, key_prefix, version: key
    }
}
# Authentication
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)
INSTALLED_APPS += [
    # The Django sites framework is required
    'django.contrib.sites',
    # Core
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Login 3rd providers
    'allauth.socialaccount.providers.amazon',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.linkedin_oauth2',
    'allauth.socialaccount.providers.twitter'
]
SITE_ID = 1
ACCOUNT_ADAPTER = 'allauth.account.adapter.DefaultAccountAdapter'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
LOGIN_REDIRECT_URL = 'index'
ACCOUNT_LOGOUT_REDIRECT_URL = 'index'
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True