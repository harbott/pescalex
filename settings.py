# Django production settings for pescalex project.
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',           # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'pescalex',                                                         
        'USER': 'pescalex',                      
        'PASSWORD': 'fishyfishy',                 
        'HOST': '',                                                         # Set to empty string for localhost. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Date format
DATE_FORMAT = 'd j Y'
DATETIME_FORMAT = 'd j Y H:i'
DATETIME_ADMIN_FORMAT = '%d %b %Y %H:%M'      # Custom setting not used natively by Django

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False
USE_L10N = False

# Get project path automatically
from os import path as os_path
PROJECT_PATH = os_path.abspath(os_path.split(__file__)[0])

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = PROJECT_PATH + '/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 's^z3!+--avc%pifu38k0zmnlzkisqqz!23tc!b&)e3i+$@1(ec'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'pescalex.urls'

TEMPLATE_DIRS = (
    os_path.join(PROJECT_PATH, 'templates'),
	#os_path.join(PROJECT_PATH, 'apps/templatetags/templatetags/templates'),    
)

FIXTURE_DIRS = (
	os_path.join(PROJECT_PATH, 'fixtures/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'pescalex.apps.courses',
    'pescalex.apps.glossaries',
    'pescalex.apps.languages',
    'pescalex.apps.news',
    'pescalex.apps.users',
)

# Auth backend to handle email address
AUTHENTICATION_BACKENDS = (
    'pescalex.backends.EmailAuthBackEnd',
    'django.contrib.auth.backends.ModelBackend',
)

# Handle file uploads
FILE_UPLOAD_TEMP_DIR = PROJECT_PATH + '/temp/'
FILE_UPLOAD_PERMISSIONS = 0777

UPLOADS_ROOT = PROJECT_PATH +  '/uploads/'

# Domain name
DOMAIN_NAME = 'http://www.pescalex.org'
DEFAULT_FROM_EMAIL = 'no-reply@pescalex.org'

# Import server specific settings
try:
    from settings_local import *
except ImportError:
    pass
