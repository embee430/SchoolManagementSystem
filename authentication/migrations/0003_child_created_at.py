# Generated by Django 5.1 on 2024-09-06 09:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_child'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
