# Generated by Django 5.0.2 on 2024-02-17 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_berries_price_decor_price_inscription_price_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price',
            options={'verbose_name': 'Цена', 'verbose_name_plural': 'Цены'},
        ),
    ]
