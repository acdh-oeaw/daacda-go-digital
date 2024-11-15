import os

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(os.path.join(__file__, "../")))
)

ACDH_IMPRINT_URL = "https://imprint.acdh.oeaw.ac.at/"
REDMINE_ID = 11260
BOMB_GROUP_LABEL = "bomb group"
AIR_FORCE_LABEL = "airforce division"
SQUAD_LABEL = "squadroon"

if os.environ.get("DEBUG", False):
    DEBUG = True
else:
    DEBUG = False
ADD_ALLOWED_HOST = os.environ.get("ALLOWED_HOST", "*")
SECRET_KEY = os.environ.get("SECRET_KEY", "TZRHHwasdfsadfdsafkljlxö7639827249324GV")

ALLOWED_HOSTS = [
    "127.0.0.1",
    "0.0.0.0",
    ADD_ALLOWED_HOST,
]


INSTALLED_APPS = [
    "dal",
    "dal_select2",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "crispy_bootstrap4",
    "django_filters",
    "django_tables2",
    "rest_framework",
    "ckeditor",
    "ckeditor_uploader",
    "leaflet",
    "idprovider",
    "webpage",
    "vocabs",
    "entities",
    "detentions",
    "browsing",
    "materials",
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "daacda.urls"

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
                "webpage.webpage_content_processors.installed_apps",
                "webpage.webpage_content_processors.is_dev_version",
                "webpage.webpage_content_processors.get_db_name",
            ],
        },
    },
]

WSGI_APPLICATION = "daacda.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "daacda"),
        "USER": os.environ.get("POSTGRES_USER", "postgres"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "postgres"),
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        "PORT": os.environ.get("POSTEGRES_PORT", "5432"),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")
STATIC_URL = "/static/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_URL = "/media/"
CKEDITOR_UPLOAD_PATH = "content/ckeditor/"

CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "full",
        "height": 300,
    },
}


VOCABS_DEFAULT_PEFIX = os.path.basename(BASE_DIR)

VOCABS_SETTINGS = {
    "default_prefix": VOCABS_DEFAULT_PEFIX,
    "default_ns": "http://www.vocabs/{}/".format(VOCABS_DEFAULT_PEFIX),
    "default_lang": "eng",
}


LEAFLET_CONFIG = {
    "MAX_ZOOM": 18,
    "DEFAULT_CENTER": (47, 16),
    "DEFAULT_ZOOM": 4,
    "TILES": [
        (
            "BASIC",
            "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
            {
                "attribution": '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>\
                    contributors',
                "maxZoom": 18,
            },
        )
    ],
}


NETVIS_TYPES = {
    "nodes": [
        {"id": "CurrentPerson", "label": "Person", "color": "#20c997"},
        {"id": "Person", "label": "Person", "color": "#006699"},
        {"id": "PrisonStation", "label": "Prisonstation", "color": "#28a745"},
        {"id": "Location", "label": "Location", "color": "#669900"},
        {"id": "Place", "label": "Location", "color": "#669900"},
        {"id": "Bomber", "label": "Bomber", "color": "#ffc107"},
    ]
}
