from os import environ
from datetime import timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = environ.get("SECRET_KEY", default="^a-^xa(@")

DEBUG = bool(environ.get("DEBUG", default="False"))

ALLOWED_HOSTS = environ.get("ALLOWED_HOSTS", default="*").split(",")

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "django_filters",
    "drf_spectacular",
    "rest_framework",
    "rest_framework_simplejwt",
]

LOCAL_APPS = [

]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": environ.get(
            "DB_ENGINE", default="django.db.backends.postgresql"
        ),
        "NAME": environ.get("DB_NAME", default="github-actions"),
        "USER": environ.get("DB_USER", default="postgres"),
        "PASSWORD": environ.get("DB_PASSWORD", default="postgres"),
        "HOST": environ.get("DB_HOST", default="localhost"),
        "PORT": environ.get("DB_PORT", default="5432"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
]

SPECTACULAR_SETTINGS = {
    "TITLE": "Donation Hub API",
    "DESCRIPTION": "API de Centro de Doações",
    "VERSION": "0.0.1",
    "SERVE_INCLUDE_SCHEMA": False,
}

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination."
    "LimitOffsetPagination",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(
        minutes=int(environ.get("ACCESS_TOKEN_LIFETIME", default=5))
    ),
    "REFRESH_TOKEN_LIFETIME": timedelta(
        minutes=int(environ.get("REFRESH_TOKEN_LIFETIME", default=10))
    ),
    "TOKEN_OBTAIN_SERIALIZER": "apps.accounts.api.serializers."
    "TokenObtainPairSerializer",
}

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Fortaleza"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "static/"

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media/"

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
