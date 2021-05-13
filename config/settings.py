import os
from loguru import logger
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ['SECRET_KEY']

SITE_DOMAIN = os.environ['SITE_DOMAIN']
ADMIN_URL = os.environ['ADMIN_URL']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'rest_framework',
    'django_filters',
    'nested_admin',
    'ckeditor',

    'backend.seo',
    'backend.home_page',
    'backend.advantages',
    'backend.orders',
    'backend.privacy',
    'backend.products',
    'backend.home_decorations',
    'backend.about',
    'backend.cubo_business',
    'backend.partnership',
    'backend.contacts',
    'backend.favorites',
    'backend.cart',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'frontend/templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 12
}



TG_BOT_TOKEN = os.environ['TG_BOT_TOKEN']
TG_ADMIN_ID = os.environ['TG_ADMIN_ID']

MEDIA_URL = 'frontend/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'frontend/media')

if os.environ['PROJECT_STATUS'] == 'DEVELOPMENT':
    try:
        from .local_settings import *

        logger.success('Local settings successfully imported ')
    except Exception as e:
        logger.error(f'Не удалось импортировать локальные наcтройки\n {e}')
elif os.environ['PROJECT_STATUS'] == 'PRODUCTION':
    try:
        from .production_settings import *

        logger.success('Production settings successfully imported ')
    except Exception as e:
        logger.error(f'Не удалось импортировать наcтройки для продакшна\n {e}')
else:
    raise Exception('Переменная окружения PROJECT_STATUS должна иметь значение "DEVELOPMENT" или "PRODUCTION"!')
