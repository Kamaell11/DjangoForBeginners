from django.shortcuts import render, get_object_or_404
from .models import Category, Shoe
from django.core.paginator import Paginator
from django.db.models import Count
from cart.models import Cart, CartItem

def home(request):
    categories = Category.objects.all()

    categories = Category.objects.annotate(product_count=Count('shoe'))
    featured_products = Shoe.objects.filter(is_featured=True)[:4]  

    category_shoes = {}
    for category in categories:
        first_shoe = Shoe.objects.filter(category=category).first()
        if first_shoe:
            category_shoes[category.name] = first_shoe

    cart_item_count = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart_item_count = CartItem.objects.filter(cart=cart).count()
    else:
        # Jeśli użytkownik nie jest zalogowany, możemy użyć sesji (jeśli wcześniej zapisano liczbę przedmiotów)
        cart_item_count = request.session.get('cart_item_count', 0)


    return render(request, 'home/index.html', {
        'categories': categories,  
        'featured_products': featured_products, 
        'category_shoes': category_shoes,  
        'banner': True,
        'title': 'Strona główna',
        'footer': True, 
        'cart_item_count': cart_item_count, 
    })


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    
    shoes_in_category = Shoe.objects.filter(category=category)

    sort_by = request.GET.get("sort_by", "")
    min_price = request.GET.get("min_price", "")
    max_price = request.GET.get("max_price", "")

    if sort_by == "price_asc":
        shoes_in_category = shoes_in_category.order_by("price")
    elif sort_by == "price_desc":
        shoes_in_category = shoes_in_category.order_by("-price")
    elif sort_by == "latest":
        shoes_in_category = shoes_in_category.order_by("-created_at")  


    if min_price and max_price:
        try:
            min_price = float(min_price)
            max_price = float(max_price)
            shoes_in_category = shoes_in_category.filter(price__gte=min_price, price__lte=max_price)
        except ValueError:
            pass 

    paginator = Paginator(shoes_in_category, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.annotate(product_count=Count("shoe"))


    cart_item_count = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart_item_count = CartItem.objects.filter(cart=cart).count()
    else:
        # Jeśli użytkownik nie jest zalogowany, możemy użyć sesji (jeśli wcześniej zapisano liczbę przedmiotów)
        cart_item_count = request.session.get('cart_item_count', 0)
    return render(
        request,
        "home/category.html",
        {
            "category": category,
            "shoes": page_obj,  
            "categories": categories, 
            "title": category.name,
            "footer": True,
            'cart_item_count': cart_item_count, 
        },
    )


def product_details(request, shoe_id):
    shoe = get_object_or_404(Shoe, id=shoe_id)
    cart_item_count = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart_item_count = CartItem.objects.filter(cart=cart).count()
    else:
        # Jeśli użytkownik nie jest zalogowany, możemy użyć sesji (jeśli wcześniej zapisano liczbę przedmiotów)
        cart_item_count = request.session.get('cart_item_count', 0)
    return render(request, 'shop/productDetails.html', {
        'shoe': shoe,
        'title': True,
        'footer': True,
        'cart_item_count': cart_item_count, 
    })


import random

def featured_shoes(request):
    featured_products = Shoe.objects.filter(is_featured=True)

    featured_products = random.sample(list(featured_products), min(len(featured_products), 4))

    context = {
        'featured_products': featured_products,
    }
    return render(request, 'home/featured_product.html', context)

def account(request):     
      data = {
       'title':'Account',
       'subTitle':'Shop',
       'subTitle2':'Account',
       'css':'<link rel="stylesheet" type="text/css" href="/static/css/variables/variable6.css"/>',
       'footer':'true',
       'script':'<script src="/static/js/vendors/zoom.js"></script>',
      }
      return render(request, "shop/account.html", data)

def cart(request):     
      data = {
       'title':'Cart',
       'subTitle':'Shop',
       'subTitle2':'Cart',
       'css':'<link rel="stylesheet" type="text/css" href="/static/css/variables/variable6.css"/>',
       'footer':'true',
       'script':'<script src="/static/js/vendors/zoom.js"></script>',
      }
      return render(request, "shop/cart.html", data)

def checkOut(request):     
      data = {
       'title':'Checkout',
       'subTitle':'Shop',
       'subTitle2':'Checkout',
       'css':'<link rel="stylesheet" type="text/css" href="/static/css/variables/variable6.css"/>',
       'footer':'true',
       'script':'<script src="/static/js/vendors/zoom.js"></script>',
      }
      return render(request, "shop/checkOut.html", data)

def fullWidthShop(request):     
      data = {
       'title':'Full Width Shop',
       'subTitle':'Shop',
       'subTitle2':'Full Width Shop',
       'css':'<link rel="stylesheet" type="text/css" href="/static/css/variables/variable6.css"/> <link rel="stylesheet" type="text/css" href="/static/css/jquery.nstSlider.min.css"/>',
       'script':'<script src="/static/js/vendors/zoom.js"></script>  <script src="/static/js/vendors/jquery.nstSlider.min.js"></script>',
       'footer':'true',
      }
      return render(request, "shop/fullWidthShop.html", data)

def groupedProducts(request):     
      data = {
       'title':'Grouped Product',
       'subTitle':'Shop',
       'subTitle2':'Grouped Product',
       'css':'<link rel="stylesheet" type="text/css" href="/static/css/variables/variable6.css"/>',
       'footer':'true',
      }
      return render(request, "shop/groupedProducts.html", data)

def productDetails(request):     
      data = {
       'title':'Product',
       'subTitle':'Shop',
       'subTitle2':'Product',
       'footer':'true',
       'script':'<script src="/static/js/vendors/zoom.js"></script>',
      }
      return render(request, "shop/productDetails.html", data)


def shop(request):     
      data = {
       'title':'Shop',
       'subTitle':'Shop',
       'subTitle2':'Shop',
       'css':'<link rel="stylesheet" type="text/css" href="/static/css/variables/variable6.css"/>',
       'css2':'<link rel="stylesheet" type="text/css" href="/static/css/jquery.nstSlider.min.css"/>',
       'footer':'true',
       'script':'<script src="/static/js/vendors/zoom.js"></script>  <script src="/static/js/vendors/jquery.nstSlider.min.js"></script>',
      }
      return render(request, "shop/shop.html", data)

def sidebarLeft(request):     
      data = {
       'title':'Slidebar Left',
       'subTitle':'Shop',
       'subTitle2':'Slidebar Left',
       'css':'<link rel="stylesheet" type="text/css" href="/static/css/variables/variable6.css"/> <link rel="stylesheet" type="text/css" href="/static/css/jquery.nstSlider.min.css"/>',
       'script':'<script src="/static/js/vendors/zoom.js"></script>  <script src="/static/js/vendors/jquery.nstSlider.min.js"></script>',
       'footer':'true',
      }
      return render(request, "shop/sidebarLeft.html", data)

def sidebarRight(request):     
      data = {
       'title':'Slidebar Right',
       'subTitle':'Shop',
       'subTitle2':'Slidebar Right',
       'css':'<link rel="stylesheet" type="text/css" href="/static/css/variables/variable6.css"/> <link rel="stylesheet" type="text/css" href="/static/css/jquery.nstSlider.min.css"/>',
       'script':'<script src="/static/js/vendors/zoom.js"></script>  <script src="/static/js/vendors/jquery.nstSlider.min.js"></script>',
      }
      return render(request, "shop/sidebarRight.html", data)

def variableProducts(request):     
      data = {
       'title':'Variable Product',
       'subTitle':'Shop',
       'subTitle2':'Variable Product',
       'script':'<script src="/static/js/vendors/jquery.nstSlider.min.js"></script> <script src="/static/js/vendors/zoom.js"></script>',
       'footer':'true',
      }
      return render(request, "shop/variableProducts.html", data)