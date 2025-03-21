from .base import *

# SECURITY WARNING: Don't run with debug turned on in production!
DEBUG = False

# Hosts that are allowed to serve this Django project
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Database configuration (using SQLite for development)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": os.environ["POSTGRES_HOST"],
        "PORT": int(os.environ["POSTGRES_DB_PORT"]),
    }
}