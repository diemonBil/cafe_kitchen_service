from django.contrib import admin
from django.urls import path, include

from kitchen import views

app_name = "kitchen"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('logout/', views.logoutView, name='logout'),
    path("", include("kitchen.urls")),  # підключаємо urls.py з додатку kitchen
]
