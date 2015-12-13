SECRET_KEY = '******************' ### Should be same across all cache servers.

#ALLOWED_HOSTS = [ '*' ]

TIME_ZONE = 'UTC'

#DOCUMENTATION_URL = "http://graphite.readthedocs.org/"

#LOG_RENDERING_PERFORMANCE = True
#LOG_CACHE_PERFORMANCE = True
#LOG_METRIC_ACCESS = True
#DEBUG = True

MEMCACHE_HOSTS = ['1.2.3.4:11211', '5.6.7.8:11211']
#DEFAULT_CACHE_DURATION = 60 # Cache images and data for 1 minute

WHISPER_DIR = '/opt/graphite_data/whisper'

DATABASES = {
    'default': {
        'NAME': '/opt/graphite/storage/graphite.db',
        'ENGINE': 'django.db.backends.sqlite3',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''
    }
}


CARBONLINK_HOSTS = ["127.0.0.1:7012:1", "127.0.0.1:7022:2"]
#CARBONLINK_TIMEOUT = 1.0
CARBONLINK_QUERY_BULK = False