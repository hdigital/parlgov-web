"""Django settings for web project.

https://docs.djangoproject.com/en/stable/topics/settings/
https://docs.djangoproject.com/en/stable/ref/settings/
"""

import os
import warnings
from pathlib import Path

import environ

from django.core.management.utils import get_random_secret_key

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Environment variables

# see ".env.example" for project documentation of environment variables
# set environment variables in production (e.g. Docker build, Heroku config)

env = environ.Env()

# load local '.env' file -- file not in version control, mainly for development
environ.Env.read_env(os.path.join(BASE_DIR, "config/.env"))

# get environment variables and set default values
ENV_CACHES = env.cache_url("CACHE_URL", default="dummycache://")
ENV_DEBUG = env.bool("DJANGO_DEBUG", default=False)
ENV_SECRET_KEY = env.str("SECRET_KEY", default=get_random_secret_key())
ENV_ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])
ENV_SSL_REQUIRED = env.bool("SSL_REQUIRED", default=False)
ENV_DATABASES = env.db_url(
    "DATABASE_URL", default=f"sqlite:///{BASE_DIR / 'parlgov.sqlite'}"
)


# General settings

# see checklist for production settings
# See https://docs.djangoproject.com/en/stable/howto/deployment/checklist/

# https://docs.djangoproject.com/en/stable/ref/settings/#debug
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENV_DEBUG

# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-SECRET_KEY
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ENV_SECRET_KEY

# https://docs.djangoproject.com/en/stable/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ENV_ALLOWED_HOSTS


# Application definition
# https://docs.djangoproject.com/en/stable/ref/settings/#installed-apps

INSTALLED_APPS = [
    # Local
    "apps.base.apps.BaseConfig",
    "apps.data.core.apps.DataCoreConfig",
    "apps.data.parties.apps.DataPartiesConfig",
    "apps.data.elections.apps.DataElectionsConfig",
    "apps.data.cabinets.apps.DataCabinetsConfig",
    "apps.docs.apps.DocsConfig",
    "apps.pages.apps.PageConfig",
    "apps.views_data.apps.ViewsDataConfig",
    "apps.api.apps.ApiConfig",
    # Django
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    # Third party
    "rest_framework",
]


# Middleware
# https://docs.djangoproject.com/en/stable/ref/settings/#middleware

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # WhiteNoise: "above all" after SecurityMiddleware — see docs (link below)
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # option cache -- see settings below
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    # option cache -- see settings below
    "django.middleware.cache.FetchFromCacheMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# Url import path // moved into apps folder
# https://docs.djangoproject.com/en/stable/ref/settings/#root-urlconf

ROOT_URLCONF = "apps.urls"


# Templates
# https://docs.djangoproject.com/en/stable/ref/settings/#templates

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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


# WSGI application path (for Gunicorn WSGI Server)
# https://docs.djangoproject.com/en/stable/ref/settings/#wsgi-application

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases

DATABASES = {"default": ENV_DATABASES}


# Password validation
# https://docs.djangoproject.com/en/stable/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 16,
        },
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/stable/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Europe/Berlin"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/stable/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
# WhiteNoise to serve static files in production (use collectstatic on deploy)
# http://whitenoise.evans.io/en/stable/django.html
STATIC_ROOT = BASE_DIR / "staticfiles"
# setting below needs collectstatic and may break testing — see also
# http://whitenoise.evans.io/en/stable/django.html#storage-troubleshoot
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
# STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
# static files names are changed (MD5 hash added) by storage engine
# https://docs.djangoproject.com/en/stable/ref/contrib/staticfiles/#manifeststaticfilesstorage


# Default primary key field type
# https://docs.djangoproject.com/en/stable/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Cache framework
# https://docs.djangoproject.com/en/stable/topics/cache/#filesystem-caching
CACHES = {"default": ENV_CACHES}

CACHE_MIDDLEWARE_ALIAS = "default"
CACHE_MIDDLEWARE_SECONDS = 60 * 60 * 24  # seconds of caching // 1 day
CACHE_MIDDLEWARE_KEY_PREFIX = ""


# Security (SSL/HTTPS)
# https://docs.djangoproject.com/en/stable/topics/security/#ssl-https

if ENV_SSL_REQUIRED:  # pragma: no cover
    SECURE_HSTS_SECONDS = 60 * 60 * 24 * 31 * 1  # 1 month
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True


# ADDITIONAL SETTINGS // DJANGO

DATE_FORMAT = "Y-m-d"
LOGIN_REDIRECT_URL = "page:home"
LOGOUT_REDIRECT_URL = "page:home"

# Transitional setting from Django 5.0 (deprecated in 5.0, removed in 6.0)
FORMS_URLFIELD_ASSUME_HTTPS = True
# Suppress specific deprecation warning for transitional setting
warnings.filterwarnings(
    "ignore",
    message="The FORMS_URLFIELD_ASSUME_HTTPS transitional setting is deprecated.",
    category=DeprecationWarning,
)

# ADDITIONAL SETTINGS // THIRD PARTY PACKAGES

# Django REST framework (DRF)
# https://www.django-rest-framework.org/api-guide/settings/

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_FILTER_BACKENDS": ["rest_framework.filters.SearchFilter"],
}


# ADDITIONAL SETTINGS // DEVELOPMENT

if ENV_DEBUG:  # pragma: no cover
    # django-debug-toolbar configs
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

    INTERNAL_IPS = ["127.0.0.1"]

    INSTALLED_APPS += ["debug_toolbar"]

    MIDDLEWARE = [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ] + MIDDLEWARE

    #  OpenAPI schema generation
    # https://drf-spectacular.readthedocs.io/en/latest/readme.html#installation

    INSTALLED_APPS += [
        "django_extensions",
        "drf_spectacular",
        "import_export",
    ]

    REST_FRAMEWORK["DEFAULT_SCHEMA_CLASS"] = "drf_spectacular.openapi.AutoSchema"

    SPECTACULAR_SETTINGS = {
        "TITLE": "ParlGov API",
        "DESCRIPTION": (
            "Parliaments and Governments Database (ParlGov): "
            "Data on parties, elections, and cabinets"
        ),
    }
