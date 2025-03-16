from django.contrib import admin
from django.urls import path, include

from kitchen import views

app_name = "kitchen"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cook-list/', views.CookListView.as_view(), name='cook_list'),
    path('cook-list/create/', views.CookListCreateView.as_view(), name='cook_create'),
    path('accounts/', include('django.contrib.auth.urls'))
]
