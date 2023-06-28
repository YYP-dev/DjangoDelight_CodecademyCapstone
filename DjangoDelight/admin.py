from django.contrib import admin
from .models import Menu,Ingredients,Purchase

# Register your models here.
admin.site.register([Menu,Ingredients,Purchase])