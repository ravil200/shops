from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=55, verbose_name='Название')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='cotegory', null=True,
                                on_delete=models.SET_NULL, verbose_name='Категория')
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение', upload_to='product/%Y/%m/%d')
    price = models.FloatField(verbose_name='Цена')
    created_at = models.DateField(auto_now=False, verbose_name='Дата создания')
    end_at = models.DateField(auto_now=False, verbose_name='Дата окончания')

    def __str__(self) -> str:
        return f'Продукт: {self.title}\n Категория: {self.category.title}'

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукт'