from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, DecimalValidator


class Category(models.Model):
    name = models.CharField('Имя категории', max_length=200, db_index=True)
    slug = models.SlugField('Название в виде url', max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        related_name='products',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    name = models.CharField('Имя', max_length=200, db_index=True)
    slug = models.SlugField('Название в виде url', max_length=200, db_index=True, unique=True)
    image = models.ImageField('Изображение', null=True, blank=True)
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField(
        'Цена',
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0), DecimalValidator(8, 2)],
    )
    stock = models.PositiveIntegerField('Остатки')
    available = models.BooleanField('Доступно', default=True)
    created = models.DateTimeField('Время создания', auto_now_add=True)
    updated = models.DateTimeField('Время изменения', default=timezone.now)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
