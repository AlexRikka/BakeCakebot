# Generated by Django 5.0.2 on 2024-02-17 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_rename_adress_cake_address_remove_client_duration_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cake',
            old_name='datetime',
            new_name='delivery_time',
        ),
    ]
