from django.contrib import admin
from django.urls import path, include

# Main URL configuration for the project
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("kitchen.urls")),  # підключаємо urls.py з додатку kitchen
]
