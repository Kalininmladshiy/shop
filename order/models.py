from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, DecimalValidator
from django.urls import reverse

from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    name = models.CharField('Имя категории', max_length=200, db_index=True)
    slug = models.SlugField('Название в виде url', max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('order:product_list_by_category', args=[self.slug])


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

    def get_absolute_url(self):
        return reverse('order:product_detail', args=[self.slug])


class Order(models.Model):
    first_name = models.CharField(
        'Имя клиента',
        max_length=50,
        db_index=True,
    )
    last_name = models.CharField(
        'Фамилия клиента',
        max_length=50,
        blank=True,
        db_index=True,
    )
    phonenumber = PhoneNumberField(
        'Номер владельца',
        db_index=True,
    )
    email = models.EmailField('Электронная почта')
    address = models.CharField(
        'Адрес',
        max_length=50,
        blank=True,
        db_index=True,
    )
    created = models.DateTimeField(
        'Время создания',
        null=True,
        db_index=True,
        default=timezone.now,
    )
    updated = models.DateTimeField(
        'Время обновления',
        null=True,
        blank=True,
        db_index=True,
        auto_now=True
    )
    paid = models.BooleanField('Оплачен', default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        verbose_name='Заказ',
        related_name='items',
        null=True,
    )
    product = models.ForeignKey(
        Product,
        verbose_name='Продукт',
        related_name='order_items',
        on_delete=models.SET_NULL,
        null=True,
    )
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('Количество', null=True)

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
