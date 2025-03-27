import json  # Added import
from django.test import TestCase, Client
from django.urls import reverse
from users.models import CustomUser as User
from shop.models import Shoe, Category
from .models import Cart, CartItem
from orders.models import Order

class CartViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Test Category')
        self.shoe = Shoe.objects.create(
            name='Test Shoe', 
            price=100,
            category=self.category
        )

    def test_add_to_cart(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('cart:add_to_cart', args=[self.shoe.id]))
        self.assertRedirects(response, reverse('cart:cart'))
        cart = Cart.objects.get(user=self.user)
        self.assertEqual(cart.items.count(), 1)

    def test_cart_detail(self):
        Cart.objects.create(user=self.user)
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('cart:cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart_detail.html')

    def test_remove_from_cart(self):
        cart = Cart.objects.create(user=self.user)
        cart_item = CartItem.objects.create(cart=cart, shoe=self.shoe)
        self.client.login(username='testuser', password='12345')

        response = self.client.get(reverse('cart:remove_from_cart', args=[cart_item.id]))
        self.assertRedirects(response, reverse('cart:cart'))
        self.assertFalse(CartItem.objects.filter(id=cart_item.id).exists())

    def test_update_cart_item(self):
        cart = Cart.objects.create(user=self.user)
        cart_item = CartItem.objects.create(cart=cart, shoe=self.shoe, quantity=1)
        self.client.login(username='testuser', password='12345')

        response = self.client.post(reverse('cart:update_cart_item', args=[cart_item.id]), {'quantity': '3'})
        self.assertEqual(response.status_code, 200)
        cart_item.refresh_from_db()
        self.assertEqual(cart_item.quantity, 3)

    def test_create_order(self):
        cart = Cart.objects.create(user=self.user)
        CartItem.objects.create(cart=cart, shoe=self.shoe, quantity=2)
        self.client.login(username='testuser', password='12345')

        response = self.client.post(
            reverse('cart:create_order'),
            data=json.dumps({'shipping_method': 'flat_rate'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Order.objects.filter(user=self.user).exists())