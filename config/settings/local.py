from .base import *  # noqa

SECRET_KEY = 'vip^*hgb+d^l@11c7acdw#9o@hx^c_*4c8%_c(mon(fsrsijag'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
