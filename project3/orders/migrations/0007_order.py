# Generated by Django 3.0 on 2020-06-28 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0006_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_completed', models.BooleanField(default=False)),
                ('dinnerplatter', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orders.DinnerPlatter')),
                ('pasta', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Pasta')),
                ('pizza', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Pizza')),
                ('salad', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Salad')),
                ('sub', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Sub')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
