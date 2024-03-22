# Generated by Django 5.0.3 on 2024-03-22 14:07

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_photo_caption_video_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, default='empty', editable=False, populate_from='name', unique=True),
        ),
    ]
