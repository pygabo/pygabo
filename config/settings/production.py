from .base import *  # noqa

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DATA_NAME'],
        'USER': os.environ['DATA_USER'],
        'PASSWORD':os.environ['DATA_PASS'],
        'HOST': os.environ['DATA_HOST'],
        'PORT': '5432',
    }
}

# STATIC
# ------------------------
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


INSTALLED_APPS += ['gunicorn']  # noqa F405
