# Generated by Django 5.0.2 on 2024-02-16 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cake',
            options={'verbose_name': 'Тортик', 'verbose_name_plural': 'Тортики'},
        ),
    ]
