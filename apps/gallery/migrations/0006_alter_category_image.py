# Generated by Django 5.0.3 on 2024-04-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_remove_video_downloads_downloadvideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='https://res.cloudinary.com/dq0ow9lxw/image/upload/v1712837648/fallback_kw4pjb.jpg', upload_to='category/%Y/%m/%d/'),
        ),
    ]
