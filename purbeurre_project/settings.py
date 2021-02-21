"""
Django settings for purbeurre_project project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

import django_heroku
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://bf70c56efba947b2ad2f73d976713cfc@o488761.ingest.sentry.io/5549713",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

# Activate Django-Heroku
# django_heroku.settings(locals())

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'w25jxj=r+u^6*1%_vu1#j4a6t#1_6ks4hbpj$llg_p^**9fr$s'

SECRET_KEY = os.environ.get("SECRET_KEY", '7rxo>\r#"qi)y<mD`.X3\\^\x0c<k')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if os.environ.get("ENV") == "PRODUCTION":
    DEBUG = False

ALLOWED_HOSTS = ["localhost", "127.0.0.1", ".herokuapp.com","167.99.212.10","smtp.gmail.com"]

# Application definition

INSTALLED_APPS = [
    "search.apps.SearchConfig",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "debug_toolbar",
    "django.contrib.auth",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# LOGIN_REDIRECT_URL = '/search/profile/'
LOGIN_REDIRECT_URL = "/"

ROOT_URLCONF = "purbeurre_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR,"templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "purbeurre_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

""" DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3"}
} """

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",  # on utilise l'adaptateur postgresql
        "NAME": "purbeurre",  # le nom de notre base de donnees creee precedemment
        "USER": "david",  # attention : remplacez par votre nom d'utilisateur
        "PASSWORD": "Selmer!25",
        "HOST": "",
        "PORT": "5432",
    }
}

AUTHENTICATION_BACKENDS = ["search.models.EmailBackend"]
# ACCOUNT_EMAIL_VERIFICATION = 'none'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'contact.purbeurre@gmail.com'
EMAIL_HOST_PASSWORD = 'PurP8@contact'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_HOST_USER = 'apikey'
# EMAIL_HOST_PASSWORD = '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'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'contact@purbeurre.com'

# DEFAULT_FROM_EMAIL = 'TestSite Team <noreply@example.com>'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# AUTH_USER_MODEL = ''

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "fr"

TIME_ZONE = "Europe/Paris"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATIC_ROOT = str(BASE_DIR / 'staticfiles')

if os.getenv("ENV") == "PRODUCTION":
    django_heroku.settings(locals())
