# Generated by Django 5.0.2 on 2024-02-17 14:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_alter_decor_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decor',
            name='price',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='polls.price'),
        ),
    ]
