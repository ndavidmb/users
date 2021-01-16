from .base import *

#SECURITY WARNING

DEBUG = True

ALLOWED_HOSTS = []

#DATABASES

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER':get_secret('USER'),
        'PASSWORD':get_secret('PASSWORD'),
        'HOST':'localhost',
        'PORT':'5432',
    }
}

#STATIC FILES

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "../static",]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "../media"

# Email settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = get_secret('EMAIL')
EMAIL_HOST_PASSWORD = get_secret('PASSWORD_EMAIL')
EMAIL_PORT = 587