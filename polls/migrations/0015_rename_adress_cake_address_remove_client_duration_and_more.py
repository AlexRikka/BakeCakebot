# Generated by Django 5.0.2 on 2024-02-17 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_alter_price_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cake',
            old_name='adress',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='client',
            name='duration',
        ),
        migrations.AlterField(
            model_name='cake',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
