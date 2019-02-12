from .base import *

# This test runner uses temporary local file storage
TEST_RUNNER = 'factoriomaps.runner.LocalStorageDiscoverRunner'

DATABASES = {
    'default': {
        'HOST': os.environ.get('DATABASE_HOST'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': 'postgres',
        'PASSWORD': '',  # Travis CI default DB password
    }
}
