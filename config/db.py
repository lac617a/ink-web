import os
from django.conf import settings
from decouple import config
DATABASES_DEV={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES_ENV={
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':config('DB_NAME'),
        'USER':config('DB_USER'),
        'PASSWORD':config('DB_PASS'),
        'HOST':config('DB_HOST'),
        'PORT':'5432',
    }
}