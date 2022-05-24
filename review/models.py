from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from product.models import Product

class Review(models.Model):

    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE, verbose_name='Автор'
    )
    product = models.ForeignKey(
        to=Product, verbose_name='Продукт', on_delete=models.CASCADE
    )
    text = models.TextField(blank=True, null=True)
    rating = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'