# Generated by Django 4.2.5 on 2023-11-05 18:31

from django.db import migrations, models
import ecommerce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0016_remove_order_city_remove_order_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='order',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=ecommerce.models.Order),
        ),
    ]
