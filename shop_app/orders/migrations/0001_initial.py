# Generated by Django 4.2.9 on 2025-01-31 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('pending', 'Oczekujące'), ('shipped', 'Wysłane'), ('delivered', 'Dostarczone'), ('cancelled', 'Anulowane')], default='pending', max_length=10)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('shipped_date', models.DateTimeField(blank=True, null=True)),
                ('delivered_date', models.DateTimeField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
