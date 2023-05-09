from django.db import models

# Create your models here.
class Catigory(models.Model):
    # Sozdat kolonki kategoriy

    category_name = models.CharField(max_length=75)
    reg_date = models.DateTimeField(auto_now_add=True)

    # Vivod info v normalnom vide
    def __str__(self):
        return self.category_name


# Sozdat tablicu dlya produkta
class Product(models.Model):
    # Sozdat kolonki dlya tablici produktov
    product_name = models.CharField(max_length=125)
    product_count = models.IntegerField()
    product_prise = models.FloatField()
    product_foto = models.ImageField(upload_to='media')
    product_des = models.TextField()
    product_category = models.ForeignKey(Catigory, on_delete=models.CASCADE)

    reg_date = models.DateTimeField(auto_now_add=True)

    # Vivod v normalnom vide
    def __str__(self):
        return self.product_name


class UserCart(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_product_quantity = models.IntegerField()
    total_for_product = models.FloatField()
