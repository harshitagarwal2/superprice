# Generated by Django 2.1.3 on 2018-11-04 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superprice_api', '0002_auto_20181104_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruits',
            name='price',
            field=models.FloatField(),
        ),
    ]