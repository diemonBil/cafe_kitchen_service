from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.models import Cook


class CookListView(generic.ListView):
    model = Cook
    template_name = 'kitchen/cook_list.html'
    context_object_name = 'cook_list'

class CookListCreateView(generic.CreateView):
    model = Cook
    fields = "__all__"
    success_url = reverse_lazy('kitchen:cook_list')
    template_name = 'kitchen/cook_form.html'