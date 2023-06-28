from django.db import models

# Create your models here.
class Ingredients(models.Model):
    name = models.CharField(max_length=250)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=10, default="buah")

class Menu(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    foto = models.ImageField(upload_to="photos/", default='')

class Purchase(models.Model):
    menu_name = models.ForeignKey(Menu, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    review = models.CharField(max_length=500,default="Good")

