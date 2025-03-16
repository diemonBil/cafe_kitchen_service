from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import UpdateView, DeleteView

from kitchen.forms import CookCreationForm, DishTypeForm, DishForm
from kitchen.models import Cook, DishType, Dish

# ===========================================
# Cook Views (List, Create, Update, Delete)
# ===========================================

class CookListView(LoginRequiredMixin, generic.ListView):
    """Displays a list of all cooks (only for authenticated users)."""
    model = Cook
    template_name = "kitchen/cook_list.html"
    context_object_name = "cook_list"

class CookListCreateView(LoginRequiredMixin, generic.CreateView):
    """Allows an authenticated user to create a new cook."""
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("kitchen:cook_list")
    template_name = "kitchen/cook_form.html"

"""Allows an authenticated user to edit an existing cook."""
class CookUpdateView(LoginRequiredMixin, UpdateView):
    model = Cook
    fields = ["username", "first_name", "last_name"]
    template_name = "kitchen/cook_form.html"
    success_url = reverse_lazy("kitchen:cook_list")

"""Allows an authenticated user to delete a cook."""
class CookDeleteView(LoginRequiredMixin, DeleteView):
    model = Cook
    template_name = "kitchen/cook_confirm_delete.html"
    success_url = reverse_lazy("kitchen:cook_list")

# ===========================================
# Dish Type Views (List, Create, Update, Delete)
# ===========================================

class DishTypeListView(LoginRequiredMixin, generic.ListView):
    """Displays a list of all dish types (only for authenticated users)."""
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_types"

class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    """Allows an authenticated user to create a new dish type."""
    model = DishType
    form_class = DishTypeForm
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish_type_list")

class DishTypeUpdateView(LoginRequiredMixin, UpdateView):
    """Allows an authenticated user to update an existing dish type."""
    model = DishType
    form_class = DishTypeForm
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish_type_list")

class DishTypeDeleteView(LoginRequiredMixin, DeleteView):
    """Allows an authenticated user to delete a dish type."""
    model = DishType
    template_name = "kitchen/dish_type_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish_type_list")

# ===========================================
# Dish Views (List, Create, Update, Delete)
# ===========================================

class DishListView(LoginRequiredMixin, generic.ListView):
    """Displays a list of all dishes (only for authenticated users)."""
    model = Dish
    template_name = "kitchen/dish-list.html"
    context_object_name = "dish_list"

class DishCreateView(LoginRequiredMixin, generic.CreateView):
    """Allows an authenticated user to create a new dish."""
    model = Dish
    form_class = DishForm
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("kitchen:dish_list")

class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    """Allows an authenticated user to update an existing dish."""
    model = Dish
    fields = ["name", "description", "price", "dish_type", "cooks"]
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("kitchen:dish_list")

class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    """Allows an authenticated user to delete a dish."""
    model = Dish
    template_name = "kitchen/dish_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish_list")
