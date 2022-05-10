from http.client import CREATED
from django.db import models
from product.models import Product
from django.core.validators import MinValueValidator

class OrderLine(models.Model):
    CREATED = 'Принят'
    IN_PROCCES = 'В Процессе'
    COMPLETED = 'Готово'
    DELIVERY = 'Доставлен'
    ORDER_STATUS = [
        (CREATED, 'Принят'),
        (IN_PROCCES, 'В Процессе'),
        (COMPLETED, 'Готово'),
        (DELIVERY, 'Доставлен')
    ]
    first_name = models.CharField(max_length=255, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия пользователя')
    email = models.EmailField(verbose_name='Почта пользователя')
    address = models.CharField(verbose_name='Адрес', max_length=500)
    city = models.CharField(verbose_name='Город', max_length=200)
    order_status = models.CharField(verbose_name='Статус заказа',
                                    max_length=10, choices=ORDER_STATUS, default=CREATED)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')

    def __str__(self) -> str:
        return 'Order {}'.format(self.id)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Форма заказа'
        verbose_name_plural = 'Форма заказов'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class Order(models.Model):
    order_line = models.ForeignKey(OrderLine, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='products')
    amount = models.IntegerField(verbose_name='Количество', default=1, 
                                validators=[MinValueValidator(1)])
    total_price = models.DecimalField(max_digits=9, decimal_places=2, 
                                    blank=True, null=True,verbose_name='Общая стоимость')

    def __str__(self) -> str:
        return f'Продукт: {self.product}\n стоимость: {self.total_price}'

    def save(self, *args, **kwargs):
        self.total_price = self.product.price * self.amount
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def get_cost(self):
        return self.product.price * self.amount