from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import CookCreationForm
from kitchen.models import Cook


class CookListView(generic.ListView):
    model = Cook
    template_name = 'kitchen/cook_list.html'
    context_object_name = 'cook_list'

class CookListCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy('kitchen:cook_list')
    template_name = 'kitchen/cook_form.html'