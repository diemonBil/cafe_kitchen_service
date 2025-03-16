from django.contrib import admin
from django.urls import path, include

from kitchen import views

app_name = "kitchen"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.CookListView.as_view(), name='cook_list'),
    path('cook-list/', views.CookListView.as_view(), name='cook_list'),
    path('cook-list/create/', views.CookListCreateView.as_view(), name='cook_create'),
    path('cook-list/edit/<int:pk>/', views.CookUpdateView.as_view(), name='cook_edit'),
    path('cook-list/delete/<int:pk>/', views.CookDeleteView.as_view(), name='cook_delete'),
    path('dish-types/', views.DishTypeListView.as_view(), name='dish_type_list'),
    path('dish-types/create/', views.DishTypeCreateView.as_view(), name='dish_type_create'),
    path('dish-types/<int:pk>/update/', views.DishTypeUpdateView.as_view(), name='dish_type_update'),
    path('dish-types/<int:pk>/delete/', views.DishTypeDeleteView.as_view(), name='dish_type_delete'),

]
