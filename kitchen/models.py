from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from django.conf import settings


class DishType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name

class Cook(AbstractUser):
    years_of_experience = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )
    class Meta:
        ordering = ("username", )
    def __str__(self):
        return f"{self.username}: ({self.first_name} {self.last_name})"

class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True, max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.CASCADE,
        related_name="dishes_by_type"
    )
    cooks = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="dishes_by_cooks"
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"{self.name} (price: {self.price}, type: {self.dish_type.name if self.dish_type else 'No type'})"