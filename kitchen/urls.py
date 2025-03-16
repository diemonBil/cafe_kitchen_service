from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from kitchen import views

# Namespace for the "kitchen" app (used in templates with {% url 'kitchen:route_name' %})
app_name = "kitchen"

urlpatterns = [
    # Django admin panel
    path("admin/", admin.site.urls),

    # Cook-related views
    path("", views.CookListView.as_view(), name="cook_list"),  # Default home page - cook list
    path("cook-list/", views.CookListView.as_view(), name="cook_list"),  # List of cooks
    path("cook-list/create/", views.CookListCreateView.as_view(), name="cook_create"),  # Create a new cook
    path("cook-list/edit/<int:pk>/", views.CookUpdateView.as_view(), name="cook_edit"),  # Edit cook details
    path("cook-list/delete/<int:pk>/", views.CookDeleteView.as_view(), name="cook_delete"),  # Delete a cook

    # Dish Type (Categories) views
    path("dish-types/", views.DishTypeListView.as_view(), name="dish_type_list"),  # List of dish types
    path("dish-types/create/", views.DishTypeCreateView.as_view(), name="dish_type_create"),  # Create a new dish type
    path("dish-types/<int:pk>/update/", views.DishTypeUpdateView.as_view(), name="dish_type_update"),  # Edit dish type
    path("dish-types/<int:pk>/delete/", views.DishTypeDeleteView.as_view(), name="dish_type_delete"),  # Delete dish type

    # Dish-related views
    path("dishes/", views.DishListView.as_view(), name="dish_list"),  # List of dishes
    path("dishes/create/", views.DishCreateView.as_view(), name="dish_create"),  # Create a new dish
    path("dish/<int:pk>/update/", views.DishUpdateView.as_view(), name="dish_update"),  # Edit dish
    path("dish/<int:pk>/delete/", views.DishDeleteView.as_view(), name="dish_delete"),  # Delete dish

    # Authentication
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
]
