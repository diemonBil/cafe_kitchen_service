from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import UpdateView, DeleteView

from kitchen.forms import CookCreationForm, DishTypeForm
from kitchen.models import Cook, DishType


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    template_name = 'kitchen/cook_list.html'
    context_object_name = 'cook_list'

class CookListCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy('kitchen:cook_list')
    template_name = 'kitchen/cook_form.html'

def logoutView(request:HttpRequest) -> HttpResponse:
    logout(request)
    return render(request, 'kitchen/logout.html')

class CookUpdateView(LoginRequiredMixin, UpdateView):
    model = Cook
    fields = ['username', 'first_name', 'last_name']
    template_name = 'kitchen/cook_form.html'
    success_url = reverse_lazy('kitchen:cook_list')

class CookDeleteView(LoginRequiredMixin, DeleteView):
    model = Cook
    template_name = 'kitchen/cook_confirm_delete.html'
    success_url = reverse_lazy('kitchen:cook_list')

class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = 'kitchen/dish_type_list.html'
    context_object_name = 'dish_types'

class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    form_class = DishTypeForm
    template_name = 'kitchen/dish_type_form.html'
    success_url = reverse_lazy('kitchen:dish_type_list')

class DishTypeUpdateView(UpdateView):
    model = DishType
    form_class = DishTypeForm
    template_name = 'kitchen/dish_type_form.html'
    success_url = reverse_lazy('kitchen:dish_type_list')

class DishTypeDeleteView(DeleteView):
    model = DishType
    template_name = 'kitchen/dish_type_confirm_delete.html'
    success_url = reverse_lazy('kitchen:dish_type_list')