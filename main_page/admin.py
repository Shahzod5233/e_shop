from django.contrib import admin
from .models import Catigory, Product

# Register your models here.

# Pokazivat admin paneli
admin.site.register(Catigory)
admin.site.register(Product)