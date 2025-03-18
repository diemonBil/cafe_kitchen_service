from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import UpdateView, DeleteView

from kitchen.forms import CookCreationForm, DishTypeForm, DishForm, DishSearchForm
from kitchen.models import Cook, DishType, Dish

# ===========================================
# Cook Views (List, Create, Update, Delete)
# ===========================================

"""Displays a list of all cooks (only for authenticated users)."""
class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    template_name = "kitchen/cook_list.html"
    context_object_name = "cook_list"

"""Allows an authenticated user to create a new cook."""
class CookListCreateView(LoginRequiredMixin, generic.CreateView):
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

"""Displays a list of all dish types (only for authenticated users)."""
class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_types"

"""Allows an authenticated user to create a new dish type."""
class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    form_class = DishTypeForm
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish_type_list")


"""Allows an authenticated user to update an existing dish type."""
class DishTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = DishType
    form_class = DishTypeForm
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish_type_list")

"""Allows an authenticated user to delete a dish type."""
class DishTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = DishType
    template_name = "kitchen/dish_type_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish_type_list")

# ===========================================
# Dish Views (List, Create, Update, Delete)
# ===========================================

"""Displays a list of all dishes (only for authenticated users)."""
class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    template_name = "kitchen/dish-list.html"
    context_object_name = "dish_list"
    paginate_by = 2

    """Adds a search form to the context."""
    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishSearchForm(
            initial={"name": name}
        )
        return context

    """Filters dishes by name if a search query is provided."""
    def get_queryset(self):
        name = self.request.GET.get("name")
        queryset = Dish.objects.all()
        if name:
            return queryset.filter(name__icontains=name)
        return queryset

"""Allows an authenticated user to create a new dish."""
class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("kitchen:dish_list")

"""Allows an authenticated user to update an existing dish."""
class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = ["name", "description", "price", "dish_type", "cooks"]
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("kitchen:dish_list")

"""Allows an authenticated user to delete a dish."""
class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    template_name = "kitchen/dish_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish_list")

"""Main page displaying statistics on dishes, cooks, and dish types."""
class HomeView(generic.View):
    def get(self, request):
        context = {
            "dish_count": Dish.objects.count(),
            "cook_count": Cook.objects.count(),
            "dish_type_count": DishType.objects.count(),
        }
        return render(request, "kitchen/home.html", context)