from django.contrib.auth.forms import UserCreationForm
from kitchen.models import Cook

class CookCreationForm(UserCreationForm):
    class Meta:
        model = Cook
        fields = ["username", "first_name", "last_name", "email", "years_of_experience"]