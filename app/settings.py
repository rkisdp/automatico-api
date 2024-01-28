"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from datetime import timedelta
from os import path
from pathlib import Path

from django.utils.translation import gettext_lazy as _
from environ import Env
from rest_framework.settings import api_settings

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str(
    "SECRET_KEY",
    default="django-insecure-wnw+ena@t6xfsbjy@b%$yyy8=)-&ea8ow@ywiwtk8hyxx7j8#p",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=True)

ALLOWED_HOSTS = env.tuple("ALLOWED_HOSTS", default=())


# Application definition

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "django_filters",
    "drf_spectacular",
    "rest_framework",
    "core",
    "documentation",
    "questions",
    "security",
    "services",
    "user",
    "users",
    "vehicles",
    "workshops",
)


REST_FRAMEWORK = {
    "DEFAULT_PARSER_CLASSES": ("core.parsers.AutoMaticoJSONParser",),
    "DEFAULT_RENDERER_CLASSES": ("core.renderers.AutoMaticoJSONRenderer",),
    "DEFAULT_VERSIONING_CLASS": "core.versioning.XAutoMaticoAPIVersioning",
    "DEFAULT_VERSION": "v0.9",
    "ALLOWED_VERSIONS": ("v0.9", "v0.8"),
    "VERSION_PARAM": "version",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.OrderingFilter",
    ),
    "DEFAULT_SCHEMA_CLASS": "core.openapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "core.pagination.HeaderPagination",
    "PAGE_SIZE": 25,
    "COERCE_DECIMAL_TO_STRING": False,
    "URL_FIELD_NAME": "url",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=180),
    "UPDATE_LAST_LOGIN": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": env.str("JWT_SIGNING_KEY", default=SECRET_KEY),
    "VERIFYING_KEY": env.str("JWT_VERIFYING_KEY", default=None),
    "AUDIENCE": env.str("JWT_AUDIENCE", default=None),
    "ISSUER": env.str("JWT_ISSUER", default=None),
    "JWK_URL": env.str("JWK_URL", default=None),
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
    "TOKEN_OBTAIN_SERIALIZER": "security.serializers.AccessTokenSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
}

CORS_ALLOWED_ORIGINS = env.tuple("CORS_ALLOWED_ORIGINS", default=())
CSRF_TRUSTED_ORIGINS = env.tuple("CSRF_TRUSTED_ORIGINS", default=())

SPECTACULAR_SETTINGS = {
    "TITLE": "AutoMático API",
    "DESCRIPTION": "AutoMático API",
    "VERSION": "v0.9.0",
    "TOS": None,
    "LICENSE": None,
    "SERVE_INCLUDE_SCHEMA": False,
    "COMPONENT_SPLIT_PATCH": True,
    "COMPONENT_NO_READ_ONLY_REQUIRED": False,
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "filter": True,
        "displayRequestDuration": True,
        "syntaxHighlight.activate": True,
        "syntaxHighlight.theme": "monokai",
    },
    "COMPONENT_SPLIT_REQUEST": True,
    "SERVERS": (
        {
            "url": "http://localhost:8000",
            "description": "Local development server",
        },
    )
    if DEBUG
    else (
        {
            "url": "https://api.automatico.onunez.me",
            "description": "Production server",
        },
    ),
    "CONTACT": {
        "name": "AutoMático Team",
        "email": "automatico@onunez.me",
    },
    "DEFAULT_GENERATOR_CLASS": "core.generators.SchemaGenerator",
    "TAGS": (
        {
            "name": "auth",
            "description": "Authenticate to access more endpoints.",
        },
        {
            "name": "questions",
            "description": "Q/A.",
        },
        {
            "name": "reviews",
            "description": "Write, read and respond to reviews.",
        },
        {
            "name": "services",
            "description": "Request and manage services.",
        },
        {
            "name": "users",
            "description": "Get public and private information about users.",
        },
        {
            "name": "vehicles",
            "description": "Manage vehicles.",
        },
        {
            "name": "workshops",
            "description": "Explore and manage workshops.",
        },
        {
            "name": "deprecated",
            "description": "Deprecated endpoints.",
        },
    ),
}

MIDDLEWARE = (
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
)


ROOT_URLCONF = "app.urls"

TEMPLATES = (
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": (BASE_DIR / "templates",),
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": (
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ),
        },
    },
)


WSGI_APPLICATION = "app.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": env.str("DB_ENGINE", default="django.db.backends.sqlite3"),
        "NAME": env.str("DB_NAME", default="db.sqlite3"),
        "USER": env.str("DB_USER", default=None),
        "PASSWORD": env.str("DB_PASSWORD", default=None),
        "HOST": env.str("DB_HOST", default=None),
        "PORT": env.str("DB_PORT", default=None),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = (
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 9,
        },
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
)


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"
LANGUAGES = (
    ("en", _("English")),
    ("es", _("Spanish")),
)


TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env.str("EMAIL_HOST", default="smtp.gmail.com")
EMAIL_PORT = env.int("EMAIL_PORT", default=587)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env.str("EMAIL_HOST_USER", default=None)
DEFAULT_FROM_EMAIL = env.str("EMAIL_FROM", default=None)
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD", default=None)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

MEDIA_ROOT = path.join(BASE_DIR, "media")
MEDIA_URL = "media/"

STATIC_ROOT = path.join(BASE_DIR, "static")
STATIC_URL = "static/"

STATIC_FILES_DIR = (BASE_DIR / "static",)

api_settings.UPLOADED_FILES_USE_URL = False
api_settings.MEDIA_ROOT = MEDIA_ROOT
api_settings.MEDIA_URL = MEDIA_URL

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.UserModel"

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

APPEND_SLASH = False
