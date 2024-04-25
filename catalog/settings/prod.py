from .base import *

DEBUG = False

ADMINS = [
    ('Praise Idowu', 'ifeoluwapraise02@gmail.com'),
]

# ALLOWED_HOSTS = ['.vercel.app', '.now.sh'] 
ALLOWED_HOSTS = [".vercel.app", "localhost", "127.0.0.1"]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            #  activate for production environment For django-crispy-form
            'loaders': [
                (
                    'django.template.loaders.cached.Loader',
                    [
                        'django.template.loaders.filesystem.Loader',
                        'django.template.loaders.app_directories.Loader',
                        'path.to.custom.Loader',
                    ],
                ),
            ],
        },
    },
]

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": config("POSTGRES_HOST"),
        "PORT": config("POSTGRES_PORT"),
    }
}

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}