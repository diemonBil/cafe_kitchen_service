from .base import *

# SECURITY WARNING: Don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", "") != "False"  # Set to False in production

# Hosts that are allowed to serve this Django project
ALLOWED_HOSTS = ["127.0.0.1"]

# Database configuration (using SQLite for development)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}