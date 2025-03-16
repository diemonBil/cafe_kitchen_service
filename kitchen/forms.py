from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from kitchen.models import Cook, DishType, Dish


# Form for creating a new cook (user registration)
class CookCreationForm(UserCreationForm):
    class Meta:
        model = Cook
        fields = ["username", "first_name", "last_name", "email", "years_of_experience"]


# Form for creating and editing dish types
class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ["name"]


# Form for creating and editing dishes
class DishForm(forms.ModelForm):
    # Use a standard text input instead of a textarea for the description
    description = forms.CharField(
        widget=forms.TextInput(),
        required=False  # Make the field optional
    )

    # Use checkboxes for selecting multiple cooks
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Dish
        fields = "__all__"  # Include all fields from the Dish model
