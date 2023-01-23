from django.db import models
from django.utils import timezone

# Create your models here.
class Recipe(models.Model):
    category = (
        ("veg", "VEG"),
        ("non veg", "NON-VEG")
    )
    
    recipe_name = models.CharField(max_length=255, unique=True)
    recipe_category  = models.CharField(choices=category, max_length=255)
    ingredients = models.TextField(max_length=600, blank=True, null=True)
    dish_img = models.FileField(upload_to = 'dish-img/', max_length=555)
    recipe_desc = models.TextField(blank=False, null=False)
    added_on = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.recipe_name