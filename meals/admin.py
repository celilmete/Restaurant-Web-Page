from django.contrib import admin

# Register your models here.
from .models import Meals
from .models import Category

admin.site.register(Meals)
admin.site.register(Category)
