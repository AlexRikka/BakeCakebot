# Generated by Django 5.0.2 on 2024-02-17 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_remove_cake_price_remove_berries_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='berries',
            name='price',
        ),
        migrations.RemoveField(
            model_name='decor',
            name='price',
        ),
        migrations.RemoveField(
            model_name='inscription',
            name='price',
        ),
        migrations.RemoveField(
            model_name='level',
            name='price',
        ),
        migrations.RemoveField(
            model_name='shape',
            name='price',
        ),
        migrations.RemoveField(
            model_name='topping',
            name='price',
        ),
    ]