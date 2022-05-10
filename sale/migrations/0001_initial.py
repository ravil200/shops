# Generated by Django 4.0.3 on 2022-03-24 13:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя пользователя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия пользователя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта пользователя')),
                ('address', models.CharField(max_length=500, verbose_name='Адрес')),
                ('city', models.CharField(max_length=200, verbose_name='Город')),
                ('order_status', models.CharField(choices=[('Принят', 'Принят'), ('В Процессе', 'В Процессе'), ('Готово', 'Готово'), ('Доставлен', 'Доставлен')], default='Принят', max_length=10, verbose_name='Статус заказа')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')),
            ],
            options={
                'verbose_name': 'Форма заказа',
                'verbose_name_plural': 'Форма заказов',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество')),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Общая стоимость')),
                ('order_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='sale.orderline')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.product')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
