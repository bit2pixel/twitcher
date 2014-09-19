"""
Django settings for twitcher project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import configparser
import os
from os.path import dirname, join

config = configparser.ConfigParser()
config.read('config.ini')

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = config.get('DJANGO', 'SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'twitterapi',
    'twitcher',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'twitcher.urls'

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

WSGI_APPLICATION = 'twitcher.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/assets/'

STATIC_ROOT = join(dirname(dirname(__file__)), "assets")

STATICFILES_DIRS = (join(dirname(dirname(__file__)), "static"),)

# TEMPLATES SETTINGS
TEMPLATE_DIRS = (
    join(dirname(dirname(__file__)), "templates"),
)

# LOGIN SETTINGS
LOGIN_URL = '/login/'
LOGIN_ERROR_URL = '/login/'
LOGIN_REDIRECT_URL = '/home/'
LOGOUT_REDIRECT_URL = '/'

# TWITTER API SETTINGS
TWITTER_APP_KEY = config.get('TWITTER_API', 'TWITTER_APP_KEY')
TWITTER_APP_SECRET = config.get('TWITTER_API', 'TWITTER_APP_SECRET')
TWITTER_OAUTH_TOKEN = config.get('TWITTER_API', 'TWITTER_OAUTH_TOKEN')
TWITTER_OAUTH_TOKEN_SECRET = config.get('TWITTER_API', 'TWITTER_OAUTH_TOKEN_SECRET')
