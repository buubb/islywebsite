from pathlib import Path
from django.contrib.messages import constants as messages
import os
import environ

env = environ.Env()
env_file = Path(__file__).resolve().parent.parent / '.env'
env.read_env(env_file)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['ctf.h4ck1ngis1y.xyz']

AUTH_USER_MODEL= 'User.User'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.forms',
    'islyweb',
    'notice',
    'login',
    'introduction',
    'volunteer',
    'CTF_Challenge',
    'recruit',
    'User.apps.UserConfig',
    'django_extensions',
    'crispy_forms',
    'crispy_bootstrap5',
    'mainpage',
    'axes',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'login.middleware.CsrfFailureMiddleware',
    'axes.middleware.AxesMiddleware',
    'islyweb.middleware.RedirectMiddleware',
]

LOGOUT_REDIRECT_URL = '/'
AXES_LOCKOUT_URL = '/login/blocked/'

AXES_FAILURE_LIMIT= 5
AXES_COOLOFF_TIME= 0.5
AXES_RESET_ON_SUCCESS = True

AUTHENTICATION_BACKENDS = [
   'axes.backends.AxesBackend',
   'django.contrib.auth.backends.ModelBackend',
]

from django.contrib.messages import constants as messages_constants
MESSAGE_LEVEL=messages_constants.INFO
MESSAGE_LEVEL=messages_constants.DEBUG

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

ROOT_URLCONF = 'islyweb.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'islyweb.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT', default=''),
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
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


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/staticfiles/'
# STATICFILES_DIRS = [
#    BASE_DIR / 'static',
#]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

FORM_RENDERFORM='django.forms.renderers.TemplatesSetting'

# 로깅
#LOGGING = {
    #'version': 1,
    #'disable_existing_loggers': False,
   # 'handlers': {
       # 'file': {
       #     'level': 'DEBUG',
      #      'class': 'logging.FileHandler',
     #       'filename': '/var/log/debug.log',
    #    },
   # },
  #  'loggers': {
      #  'django': {
     #       'handlers': ['file'],
    #        'level': 'DEBUG',
   #         'propagate': True,
  #      },
 #   },
#}

APPEND_SLASH = True