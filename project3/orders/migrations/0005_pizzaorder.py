# Generated by Django 3.0 on 2020-06-23 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_dinnerplatter_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaOrder',
            fields=[
                ('pizza_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.Pizza')),
                ('extras', models.CharField(choices=[('CH', 'Cheese'), ('1', '1 Topping'), ('2', '2 Toppings'), ('3', '3 Toppings'), ('SP', 'Special')], default='CH', max_length=15)),
                ('quantity', models.IntegerField(default=1)),
            ],
            bases=('orders.pizza',),
        ),
    ]
