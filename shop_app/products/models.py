from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)  # Nazwa produktu
    description = models.TextField(blank=True, null=True)  # Opis produktu
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Cena produktu
    stock = models.IntegerField(default=0)  # Liczba sztuk na stanie
    created_at = models.DateTimeField(auto_now_add=True)  # Data dodania produktu
    updated_at = models.DateTimeField(auto_now=True)  # Data ostatniej aktualizacji produktu
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # Zdjęcie produktu

    def __str__(self):
        return self.name  # Czytelna nazwa w panelu admina
