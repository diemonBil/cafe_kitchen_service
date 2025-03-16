from django.contrib.auth.forms import UserCreationForm
from django import forms

from kitchen.models import Cook, DishType


class CookCreationForm(UserCreationForm):
    class Meta:
        model = Cook
        fields = ["username", "first_name", "last_name", "email", "years_of_experience"]

class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ['name']