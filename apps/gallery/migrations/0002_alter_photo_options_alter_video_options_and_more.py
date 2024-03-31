# Generated by Django 5.0.3 on 2024-03-31 14:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['created_at']},
        ),
        migrations.AddIndex(
            model_name='photo',
            index=models.Index(fields=['created_at'], name='gallery_pho_created_9eab74_idx'),
        ),
        migrations.AddIndex(
            model_name='video',
            index=models.Index(fields=['created_at'], name='gallery_vid_created_125e6e_idx'),
        ),
    ]