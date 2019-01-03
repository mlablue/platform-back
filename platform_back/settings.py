"""
Django settings for platform_back project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys
import logging

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "iu2q#x4!88w-!i-kkokwt!vvay%ngnv_q01orz1c#$^q1ww@_3")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TESTING = False

ENV = os.environ.get("ENV", "development")

if os.environ.get("ALLOWED_HOSTS"):
    ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")
else:
    ALLOWED_HOSTS = []

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

CORS_ORIGIN_ALLOW_ALL = True


# Application definition

INSTALLED_APPS = [
    "user",
    "rest_framework",
    "drf_yasg",
    "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "mozilla_django_oidc",  # Load after auth
    "background_task",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.admindocs",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

APPEND_SLASH = False

ROOT_URLCONF = "platform_back.urls"
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = "statics"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [PROJECT_PATH + "/templates/"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "platform_back.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME", "platform_back"),
        "USER": os.environ.get("DB_USER", "platform_back"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "platform_back"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", 5432),
        "CONN_MAX_AGE": 600,
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

AUTHENTICATION_BACKENDS = [
    "user.auth.OIDCAuthenticationBackend",
    "django.contrib.auth.backends.ModelBackend",
]

AUTH_USER_MODEL = "user.User"

PLATFORM_BACK_URL = os.environ.get("PLATFORM_BACK_URL", "http://127.0.0.1:8082")

OIDC_RP_CLIENT_ID = os.environ.get("OIDC_RP_CLIENT_ID", "952974")
OIDC_RP_CLIENT_SECRET = os.environ.get(
    "OIDC_RP_CLIENT_SECRET", "579ed56ef143e48e7464541832eb21f9e51f87d42146772b590dfafc"
)
OIDC_RP_SIGN_ALGO = os.environ.get("OIDC_RP_SIGN_ALGO", "RS256")
OIDC_RP_IDP_SIGN_KEY = os.environ.get("OIDC_RP_IDP_SIGN_KEY", None)
OIDC_RP_SCOPES = "openid email profile"
OIDC_AUTH_REQUEST_RESPONSE_TYPE = "code id_token token"
OIDC_AUTH_REQUEST_EXTRA_PARAMS = {"response_type": OIDC_AUTH_REQUEST_RESPONSE_TYPE}


OIDC_OP_ISSUER = os.environ.get("OIDC_OP_ISSUER", "http://localhost:8000")
OIDC_OP_JWKS_ENDPOINT = f"{OIDC_OP_ISSUER}/jwks"
OIDC_OP_AUTHORIZATION_ENDPOINT = f"{OIDC_OP_ISSUER}/authorize"
OIDC_OP_TOKEN_ENDPOINT = f"{OIDC_OP_ISSUER}/token"
OIDC_OP_USER_ENDPOINT = f"{OIDC_OP_ISSUER}/userinfo"
OIDC_OP_SIGNUP_URL = f"{OIDC_OP_ISSUER}/signup/"


API_URL = os.environ.get("API_URL", "http://localhost:8081")
APP_URL = os.environ.get("APP_URL", "http://localhost:8080")

MANDRILL_KEY = os.environ.get("MANDRILL_KEY", False)
MANDRILL_TEST_KEY = os.environ.get("MANDRILL_TEST_KEY", False)

ACTIVE_CAMPAIGN_EVENT_KEY = os.environ.get("ACTIVE_CAMPAIGN_EVENT_KEY", False)
ACTIVE_CAMPAIGN_KEY = os.environ.get("ACTIVE_CAMPAIGN_KEY", False)
ACTIVE_CAMPAIGN_URL = os.environ.get("ACTIVE_CAMPAIGN_URL", False)
ACTIVE_CAMPAIGN_APP_LIST_ID = os.environ.get("ACTIVE_CAMPAIGN_APP_LIST_ID", False)

WEBHOOKS_SECRET = os.environ.get("WEBHOOKS_SECRET", "123")

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("user.auth.DrfOIDCAuthentication",),
    "DEFAULT_FILTER_BACKENDS": (
        "utils.contrib.drf.filters.FilterBackendWithQuerysetWorkaround",
    ),
    "DEFAULT_PARSER_CLASSES": ("rest_framework.parsers.JSONParser",),
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}


# LOGGING EMAIL
SERVER_EMAIL = "bug@bimdata.io"
EMAIL_HOST = "smtp.mandrillapp.com"
EMAIL_HOST_PASSWORD = os.environ.get("MANDRILL_SMTP_KEY", False)
EMAIL_HOST_USER = "BIMData.io"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

SWAGGER_SETTINGS = {
    "DEEP_LINKING": True,
    "DEFAULT_AUTO_SCHEMA_CLASS": "utils.doc.CamelCaseOperationIDAutoSchema",
    "DEFAULT_FILTER_INSPECTORS": ["utils.filters.DjangoFilterDescriptionInspector"],
    "DOC_EXPANSION": "none",
    "OPERATIONS_SORTER": "alpha",
    "TAGS_SORTER": "alpha",
    "SECURITY_DEFINITIONS": {
        "Bearer": {
            "type": "apiKey",
            "description": 'Copy/paste a valid access token here prefixed with "Bearer "',
            "name": "Authorization",
            "in": "header",
        }
    },
    "USE_SESSION_AUTH": False,
    "DEFAULT_INFO": "utils.doc.API_INFO",
    "DEFAULT_API_URL": "https://api-beta.bimdata.io/doc",
}


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {"format": "[django] %(levelname)s %(asctime)s %(module)s %(message)s"}
    },
    "handlers": {
        "null": {"level": "DEBUG", "class": "logging.NullHandler"},
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "verbose",
        },
        # Warning messages are sent to admin emails
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
            "include_html": True,
        },
    },
    "loggers": {
        "django.security.DisallowedHost": {"handlers": ["null"], "propagate": False},
        "django": {
            "handlers": ["console", "mail_admins"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django.template": {
            "handlers": ["console", "mail_admins"],
            "level": "INFO",
            "propagate": True,
        },
    },
}

if ENV == "development":
    DEBUG = True

if "test" in sys.argv:  # Covers regular testing and django-coverage
    TEST_RUNNER = "django_nose.NoseTestSuiteRunner"

    # Disable migration during testsuite
    class DisableMigrations(object):
        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return None

    PASSWORD_HASHERS = (
        "django.contrib.auth.hashers.MD5PasswordHasher",  # Replace hasher with a simpler and faster hash method
    )
    DEBUG = False
    TESTING = True
    MIGRATION_MODULES = DisableMigrations()  # Disable migrations during tests
    MEDIA_ROOT = "/tmp/django-tests"
    MEDIA_URL = "/media/"

    logging.disable(logging.INFO)

    # Use default logger during tests
    LOGGING = None
