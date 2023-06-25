from django.shortcuts import render
from .models import Menu,Ingredients,Purchase

# Create your views here.
def home(request):
    menu = Menu.objects.all()

    return render(request, 'DjangoDelight/index.html',{'menu':menu})

def addIngredients(request):
    menu = Menu.objects.all()

    return render(request, 'DjangoDelight/add_ingredients.html', {'menu': menu})


