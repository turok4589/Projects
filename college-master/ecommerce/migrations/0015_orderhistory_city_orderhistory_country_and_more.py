# Generated by Django 4.2.5 on 2023-11-04 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0014_order_city_order_country_order_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistory',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
