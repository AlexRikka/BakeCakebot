from django.db import models

# Create your models here.


class Client(models.Model):
    """Клиент."""
    username = models.CharField(
        max_length=50,
        unique=True,
    )
    first_name = models.CharField(
        max_length=50,
        blank=True,
    )
    phone_number = models.CharField(
        max_length=12,
    )

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('username',)

    def __str__(self):
        return self.username


class Price(models.Model):
    '''Цена'''
    price = models.IntegerField(
    )

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'
        ordering = ('price',)

    def __str__(self):
        return str(self.price)


class Level(models.Model):
    """Уровни тортиков"""
    number_of_levels = models.CharField(
        max_length=50,
    )
    price = models.ForeignKey(
        Price,
        on_delete=models.CASCADE,
        default=0
        )

    class Meta:
        verbose_name = 'Уровни тортиков'
        verbose_name_plural = 'Уровни тортиков'
        ordering = ('number_of_levels',)

    def __str__(self):
        return self.number_of_levels


class Shape(models.Model):
    '''Форма'''
    shape = models.CharField(
        max_length=50,
    )
    price = models.ForeignKey(
        Price,
        on_delete=models.CASCADE,
        default=0
        )

    class Meta:
        verbose_name = 'Форма тортиков'
        verbose_name_plural = 'Формы тортиков'
        ordering = ('shape',)

    def __str__(self):
        return self.shape


class Topping(models.Model):
    '''Топпинг'''
    topping = models.CharField(
        max_length=50,
    )
    price = models.ForeignKey(
        Price,
        on_delete=models.CASCADE,
        default=0
        )

    class Meta:
        verbose_name = 'Топпинг'
        verbose_name_plural = 'Топпинги'
        ordering = ('topping',)

    def __str__(self):
        return self.topping


class Berries(models.Model):
    '''Ягоды'''
    berries = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    price = models.ForeignKey(
        Price,
        on_delete=models.CASCADE,
        default=0
        )

    class Meta:
        verbose_name = 'Ягоды'
        verbose_name_plural = 'Ягоды'
        ordering = ('berries',)

    def __str__(self):
        return self.berries


class Decor(models.Model):
    '''Декор'''
    decor = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    price = models.ForeignKey(
        Price,
        on_delete=models.CASCADE,
        default=0
        )

    class Meta:
        verbose_name = 'Декор'
        verbose_name_plural = 'Декор'
        ordering = ('decor',)

    def __str__(self):
        return self.decor


class Inscription(models.Model):
    '''Надпись'''
    inscription = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    price = models.ForeignKey(
        Price,
        on_delete=models.CASCADE,
        default=0
        )

    class Meta:
        verbose_name = 'Надпись'
        verbose_name_plural = 'Надпись'
        ordering = ('inscription',)

    def __str__(self):
        return self.inscription


class Cake(models.Model):
    '''Тортики'''
    number_of_levels = models.ForeignKey(
        Level,
        on_delete=models.CASCADE
        )
    shape = models.ForeignKey(
        Shape,
        on_delete=models.CASCADE
        )
    shape = models.ForeignKey(
        Topping,
        on_delete=models.CASCADE
        )
    berries = models.ForeignKey(
        Berries,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        )
    decor = models.ForeignKey(
        Decor,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        )
    inscription = models.ForeignKey(
        Inscription,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        )
    # price = models.ForeignKey(
    #     Price,
    #     on_delete=models.CASCADE,
    #     )

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='client_cake'
        )
    delivery_time = models.DateTimeField(
        blank=True,
        null=True,
        )
    address = models.CharField(
        blank=True,
        max_length=255
        )
    comment = models.TextField(
        blank=True,
        null=True,
        )

    class Meta:
        verbose_name = 'Тортик'
        verbose_name_plural = 'Тортики'

    def __str__(self):
        return f"Тортик {self.id}"
