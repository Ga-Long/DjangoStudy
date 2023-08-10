from .base import * # base.py안의 모든걸 다 가져와라

# 개발환경

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True # 개발환경이니까

ALLOWED_HOSTS = [] 

DJANGO_APPS += [
    
]
PROJECT_APPS += [ 
    
]
THIRD_PARTY_APPS += [
    'debug_toolbar',
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

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]