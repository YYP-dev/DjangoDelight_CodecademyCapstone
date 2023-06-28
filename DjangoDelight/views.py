from django.shortcuts import render
from .models import Menu,Ingredients,Purchase
from django.shortcuts import redirect

# Create your views here.
def home(request):
    menu = Menu.objects.all()

    menu_purchased = {}
    log_purchase = Purchase.objects.values()
    log_menu = Menu.objects.values()

    for i in log_purchase:
        for j in log_menu:
            if i["menu_name_id"] == j["id"]:
                menu_purchased[i["id"]] = [j["name"], i["review"], i["date"]]

    print(menu_purchased)



    return render(request, 'DjangoDelight/index.html',{'menu':menu, 'menu_purchased': menu_purchased, 'purchased': log_purchase, 'range':range(5)})

def addIngredients(request):
    #mengambil data dari input form
    if request.method == 'POST':
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        unit = request.POST.get('unit')

        #menambahkan data input ke model/database
        addition = Ingredients(name=name, quantity=quantity, unit=unit)
        addition.save()

    return redirect('ingredients')

def ingredients(request):
    ingredient = Ingredients.objects.all()

    return render(request, 'DjangoDelight/add_ingredients.html', {'ingredient': ingredient})


def purchaseView(request):
    menu = Menu.objects.all()

    return render(request, 'DjangoDelight/purchase.html', {'menu': menu})

def purchase(request):
    if request.method == 'POST':
        item_id = request.POST.get('menu-item')
        review = request.POST.get('menu-review')
        menu_item = Menu.objects.get(pk=item_id)

        # #menambahkan data input ke model/database
        # addition = Ingredients.objects.get(name="Nasi")
        # addition.quantity -= nasi
        # addition.save()

        pcs = Purchase(menu_name=menu_item, review=review)
        pcs.save()

    return redirect('home')

def recipesView(request):
    return render(request, 'DjangoDelight/recipes.html')

