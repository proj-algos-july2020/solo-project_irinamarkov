# Generated by Django 2.2 on 2020-07-20 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tea_app', '0002_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
    ]