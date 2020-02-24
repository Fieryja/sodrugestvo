# vim:fileencoding=utf-8
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

gettext = lambda s: s
DEBUG = True
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
THUMBNAIL_DEBUG = DEBUG

SECRET_KEY = 'f0dj6oyy(%jw9y*o0#fll*1*wl_lmly=84(zt&q2&!p!w)o)(0'

DEBUG = True

ALLOWED_HOSTS = ['*']


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'sorl.thumbnail',
    'cms',
    'treebeard',
    'menus',
    'sekizai',
    'codemirror2',
    'django_summernote',
    'pytils',
    'cms_plugins',
    'contents',

]


CMS_TEMPLATES = (
    ('base.html', u'Главная'),
    ('inner.html', u'Внутренние'),
)

CMS_SEO_FIELDS = True

CMS_MENU_TITLE_OVERWRITE = True


SITE_ID = 1
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',


]


ROOT_URLCONF = 'sodrugestvo.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_PATH + '/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
            ],
        },
    },
]


WSGI_APPLICATION = 'sodrugestvo.wsgi.application'



# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE = 'ru'

LANGUAGES = [
    ('ru', u'Русский')
]

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(PROJECT_PATH, "media/")

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_PATH, "media/static/")


STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static/'),
)

APPEND_SLASH = True


EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(PROJECT_PATH, "media/message")


DEFAULT_FROM_EMAIL = 'robot@propeller.su'
DEFAULT_TO_EMAIL = ['iamfiery@gmail.com', ]

CODEMIRROR_CONFIG = {'htmlMode': True, 'lineNumbers': True}


THUMBNAIL_ENGINE = 'sorl.thumbnail.engines.pil_engine.Engine'

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 5 * 60

try:
    from local_settings import *
except ImportError:
    pass