# Generated by Django 3.0 on 2020-06-23 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DinnerPlatters',
            new_name='DinnerPlatter',
        ),
        migrations.RenameModel(
            old_name='Subs',
            new_name='Sub',
        ),
        migrations.RenameModel(
            old_name='Toppings',
            new_name='Topping',
        ),
    ]
