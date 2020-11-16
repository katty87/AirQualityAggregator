from django.core.exceptions import ImproperlyConfigured

from AirQualityAggregator.settings.base import *

SECRET_KEY = '!q^vwef^38%+1a_f@icc73q6by#==)=zca)sgp)tlq&1owzox)'


def get_env_value(env_variable):
    try:
        return os.environ[env_variable]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(env_variable)
        raise ImproperlyConfigured(error_msg)


ALLOWED_HOSTS = ['*']

SECRET_KEY = get_env_value("SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'air_aggr_db',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': 'db',
        'PORT': '5432',
    }
}
