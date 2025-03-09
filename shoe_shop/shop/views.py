from django.shortcuts import render, get_object_or_404
from .models import Category, Shoe


def home(request):
    categories = Category.objects.all()
    featured_products = Shoe.objects.filter(is_featured=True)[:4]  # Limit to 6 featured shoes
    
    print(featured_products)
    return render(request, 'home/index.html', {
        'categories': categories,  
        'featured_products': featured_products, 
        'footer': True, 
    })

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    shoes_in_category = Shoe.objects.filter(category=category)
    return render(request, 'home/category.html', {
        'category': category,
        'shoes': shoes_in_category,
    })

def product_details(request, shoe_id):
    shoe = get_object_or_404(Shoe, id=shoe_id)
    return render(request, 'shop/productDetails.html', {
        'shoe': shoe,
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

def productDetails2(request):     
      data = {
       'title':'Product',
       'subTitle':'Shop',
       'subTitle2':'Product',
       'footer':'true',
       'script':'<script src="/static/js/vendors/zoom.js"></script> ',
      }
      return render(request, "shop/productDetails2.html", data)

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