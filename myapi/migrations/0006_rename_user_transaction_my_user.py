# Generated by Django 4.1.3 on 2022-11-08 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_alter_transaction_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='user',
            new_name='my_user',
        ),
    ]
