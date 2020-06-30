# Generated by Django 3.0 on 2020-06-30 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20200630_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pasta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Pasta'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pizza',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Pizza'),
        ),
        migrations.AlterField(
            model_name='order',
            name='salad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Salad'),
        ),
        migrations.AlterField(
            model_name='order',
            name='sub',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Sub'),
        ),
    ]
