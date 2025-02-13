import os
from decimal import Decimal
from dj_database_url import parse as db_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "ctrl-catalogue-6azjnskd6q-uc.a.run.app,localhost").split(",")

INSTALLED_APPS = [
    "music_publisher.apps.MusicPublisherConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_cleanup",
    "rest_framework",
    "storages",  # Added for Cloud Storage
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DATABASE_NAME", "postgres"),
        "USER": os.getenv("DATABASE_USER", "postgres"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_HOST", "/cloudsql/ctrl-catalogue:us-central1:ctrl-db"),
        "PORT": os.getenv("DATABASE_PORT", "5432"),
    }
}

# Google Cloud Storage settings
GS_BUCKET_NAME = os.getenv("GS_BUCKET_NAME", "ctrl-music-static-files")
DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
GS_AUTO_CREATE_BUCKET = True
GS_DEFAULT_ACL = "publicRead"

STATIC_URL = f"https://storage.googleapis.com/{GS_BUCKET_NAME}/static/"
MEDIA_URL = f"https://storage.googleapis.com/{GS_BUCKET_NAME}/media/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

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

WSGI_APPLICATION = "dmp_project.wsgi.application"

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

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOGIN_URL = "/login/"
DATA_UPLOAD_MAX_NUMBER_FIELDS = None
CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
SECURE_HSTS_SECONDS = 0 if DEBUG else 300
SECURE_HSTS_PRELOAD = not DEBUG
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = not DEBUG

# Publisher information
PUBLISHER_NAME = os.getenv("PUBLISHER_NAME", "CTRL Space Records")
PUBLISHER_CODE = os.getenv("PUBLISHER_CODE", "000")
PUBLISHER_IPI_NAME = os.getenv("PUBLISHER_IPI_NAME")
if not PUBLISHER_IPI_NAME:
    raise ValueError("Missing PUBLISHER_IPI_NAME environment variable")
PUBLISHER_IPI_BASE = os.getenv("PUBLISHER_IPI_BASE", None)
PUBLISHER_SOCIETY_PR = os.getenv("PUBLISHER_SOCIETY_PR", "101")
PUBLISHER_SOCIETY_MR = os.getenv("PUBLISHER_SOCIETY_MR", "88")
PUBLISHER_SOCIETY_SR = os.getenv("PUBLISHER_SOCIETY_SR", None)

PUBLISHING_AGREEMENT_PUBLISHER_PR = Decimal(
    os.getenv("PUBLISHING_AGREEMENT_PUBLISHER_PR", "0.15")
)
PUBLISHING_AGREEMENT_PUBLISHER_MR = Decimal(
    os.getenv("PUBLISHING_AGREEMENT_PUBLISHER_MR", "1.0")
)
PUBLISHING_AGREEMENT_PUBLISHER_SR = Decimal(
    os.getenv("PUBLISHING_AGREEMENT_PUBLISHER_SR", "1.0")
)

OPTION_FORCE_CASE = os.getenv("OPTION_FORCE_CASE")

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
    ]
}
