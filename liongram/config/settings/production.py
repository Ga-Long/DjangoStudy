from .base import * # base.py안의 모든걸 다 가져와라

# 운영환경

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False # 운영하는 서버에서는 debug가 켜져있을 필요x

ALLOWED_HOSTS = [] 

DJANGO_APPS += [
    
]
PROJECT_APPS += [ 
    
]
THIRD_PARTY_APPS += [

]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'static'
