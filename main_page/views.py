from django.shortcuts import render, redirect
from .models import Catigory, Product
from . import models
from .forms import SearchForm

from telebot import TeleBot

bot = TeleBot('5704405413:AAHoxuYS5ROyZIW8LmJw-73AsywtseLYIWM', parse_mode='HTML')
admin_id = 2085925643

# Create your views here.


def index(request):
    all_categories = models.Catigory.objects.all()
    all_products = models.Product.objects.all()
    search_bar = SearchForm()

    context = {'all_catigories': all_categories, 'all_products': all_products, 'form': search_bar}

    if request.method == "POST":
        product_find = request.POST.get('search_product')
        try:
            search_result = models.Product.objects.get(product_name=product_find)
            return redirect(f'/item/{search_result.id}')

        except:
            return redirect("/")

    # Peredaem na front

    return render(request, 'index.html', context)


def get_exact_product(request, pk):
    find_product_from_db = models.Product.objects.get(id=pk)

    context = {'product': find_product_from_db}
    if request.method == 'POST':
        models.UserCart.objects.create(user_id=request.user.id,
                                       user_product=find_product_from_db,
                                       user_product_quantity=request.POST.get('user_product_quantity'),
                                       total_for_product=find_product_from_db.product_prise*int(request.POST.get('user_product_quantity')))
        return redirect('/cart')

    return render(request, 'exact_product.html', context)


def current_categogory(request, pk):
    category = models.Catigory.objects.get(id=pk)

    cotext = {'products': category}

    return render(request, 'current_categories.html', cotext)


def get_exact_category(request, pk):
    exact_category = models.Catigory.objects.get(id=pk)

    category_products = models.Product.objects.filter(product_category=exact_category)

    return render(request, 'exact_category.html', {'category_products': category_products})


def get_user_cart(request):
    user_cart = models.UserCart.objects.filter(user_id=request.user.id)
    return render(request, 'user_cart.html', {'cart': user_cart})


def complete_order(request):
    user_cart = models.UserCart.objects.filter(user_id=request.user.id)

    result_message = 'Новый заказ\n\n'
    total_for_all_cart = 0
    for cart in user_cart:
        result_message += f'<b>{cart.user_product}</b> x {cart.user_product_quantity}'

        total_for_all_cart += cart.total_for_product

    result_message += f'\n--------------\n<b>Itog: {total_for_all_cart}sum</b>'

    bot.send_message(admin_id, result_message)

    return redirect('/')
