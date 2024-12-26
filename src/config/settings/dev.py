from config.settings import BASE_DIR
DEBUG = True

MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

LOGGING = {
    # TODO: add formatters
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR.parent / 'logs/server.log',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

Q_CLUSTER = {
    'name': 'django-q',
    'timeout': 60,
    'orm': 'default'
}

REDIS_CONFIG = {
    'HOST': 'localhost',
    'PORT': '6379'
}
