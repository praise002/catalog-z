# Generated by Django 5.0.3 on 2024-04-01 18:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_downloadphoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='downloads',
        ),
        migrations.AlterField(
            model_name='downloadphoto',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='downloads', to='gallery.photo'),
        ),
    ]
