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

def shop(request):
    shoes = Shoe.objects.all()

    # Obsługa sortowania
    sort_by = request.GET.get("sort_by", "")
    if sort_by == "price_asc":
        shoes = shoes.order_by("price")
    elif sort_by == "price_desc":
        shoes = shoes.order_by("-price")
    elif sort_by == "latest":
        shoes = shoes.order_by("-created_at")

    # Paginacja
    paginator = Paginator(shoes, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.annotate(product_count=Count("shoe"))

    cart_item_count = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart_item_count = CartItem.objects.filter(cart=cart).count()
    else:
        cart_item_count = request.session.get("cart_item_count", 0)

    return render(request, "shop/shop.html", {
        "shoes": page_obj,
        "categories": categories,
        "title": "Shop",
        "footer": True,
        "paginator": paginator,
        "cart_item_count": cart_item_count,
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


