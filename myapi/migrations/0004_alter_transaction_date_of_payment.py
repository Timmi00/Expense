# Generated by Django 4.1.3 on 2022-11-08 21:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_transaction_date_of_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date_of_payment',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='время транзакции'),
        ),
    ]