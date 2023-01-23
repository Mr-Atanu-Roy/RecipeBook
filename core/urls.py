from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('view-recipe/<int:pk>', view_recipe),
]