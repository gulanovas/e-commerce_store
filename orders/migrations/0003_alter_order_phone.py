# Generated by Django 4.2.1 on 2023-05-17 19:12

from django.db import migrations, models
import orders.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_id_alter_orderproduct_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.PositiveIntegerField(validators=[orders.models.validate_length]),
        ),
    ]