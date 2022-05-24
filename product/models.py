from django.db import models

class Category(models.Model):

    name = models.CharField(
        max_length=150, verbose_name='Название', unique=True
    )
    slug = models.SlugField(max_length=150, primary_key=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):

    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(
        blank=True, null=True, verbose_name='Описание'
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена'
    )
    category = models.ForeignKey(
        to=Category, on_delete=models.CASCADE,
        related_name='product', verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title