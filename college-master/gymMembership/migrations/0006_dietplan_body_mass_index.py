# Generated by Django 4.2.5 on 2023-10-21 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymMembership', '0005_alter_excecise_videos'),
    ]

    operations = [
        migrations.AddField(
            model_name='dietplan',
            name='body_mass_index',
            field=models.IntegerField(null=True),
        ),
    ]
