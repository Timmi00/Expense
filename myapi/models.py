from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Transaction(models.Model):
    amount = models.DecimalField(
        verbose_name='Сумма',
        max_digits=9,
        decimal_places=2
    )
    my_user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name='пользователь',
        default='1'
    )
    date_of_payment = models.DateTimeField(
        default=now,
        verbose_name='время транзакции'
    )
    category = models.ForeignKey(
        'Categories',
        on_delete=models.CASCADE
    )
    organization = models.ForeignKey(
        'Organizations',
        on_delete=models.CASCADE
    )
    description = models.CharField(
        verbose_name='Описание',
        max_length=140
    )

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'transactions'
        verbose_name = 'транзакция'
        verbose_name_plural = 'транзакции'
        ordering = (
            'date_of_payment',
            'amount'
        )


class Categories(models.Model):
    category_name = models.CharField(
        verbose_name='Имя категории',
        max_length=60,
        unique=True
    )

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'categories'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = (
            'category_name',
        )


class Organizations(models.Model):
    organization_name = models.CharField(
        verbose_name='Название организации',
        max_length=60
    )

    def __str__(self):
        return self.organization_name

    class Meta:
        db_table = 'organizations'
        verbose_name = 'организация'
        verbose_name_plural = 'организации'
        ordering = (
            'organization_name',
        )
