# Generated by Django 5.0.3 on 2024-03-13 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='Quisque eleifend mi et nisi eleifend pretium. Duis porttitor accumsan arcu id rhoncus. Praesent fermentum venenatis ipsum, eget vestibulum purus. Nulla ut scelerisque elit, in fermentum ante. Aliquam congue mattis erat, eget iaculis enim posuere nec. Quisque risus turpis, tempus in iaculis. 120-240 Fusce eleifend varius tempus Duis consectetur at ligula 10660')),
                ('email', models.EmailField(default='info@comapany.com', max_length=254)),
                ('tel', models.CharField(default='010-020-0340')),
                ('url', models.URLField(default='www.comapany.com')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('subject', models.CharField(choices=[('Sales and Marketing', 'Sales and Marketing'), ('Creative Design', 'Creative Design'), ('UI/UX', 'UI/UX')], default='UI/UX', max_length=200)),
                ('message', models.TextField(verbose_name='Message')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(choices=[('CO-Founder', 'CO-Founder'), ('General Manager', 'General Manager'), ('Chief Executive Officer', 'Chief Executive Officer'), ('Chief Marketing Officer', 'Chief Marketing Officer'), ('Accounting Executive', 'Accounting Executive'), ('Creative Art Director', 'Creative Art Director')], max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('photo', models.ImageField(upload_to='team/')),
                ('fb', models.URLField(default='https://www.facebook.com', verbose_name='Facebook')),
                ('tw', models.URLField(default='https://www.twitter.com/', verbose_name='Twitter')),
                ('ln', models.URLField(default='https://www.linkedin.com/', verbose_name='Linkedin')),
            ],
        ),
        migrations.CreateModel(
            name='SiteDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='About Catalog-Z')),
                ('description', models.TextField(default='Pellentesque urna odio, scelerisque eu mauris vitae, vestibulum sodales neque. Ut augue justo, tincidunt nec aliquet ac, cursus vel augue. Suspendisse vel quam imperdiet, sodales tellus sed, ullamcorper lorem. Suspendisse id consequat risus. Aliquam varius posuere nunc, nec imperdiet neque condimentum at. Aenean porta eleifend venenatis. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.')),
                ('maps_url', models.URLField(default='https://maps.google.com/maps?q=Av.+L%C3%BAcio+Costa,+Rio+de+Janeiro+-+RJ,+Brazil&t=&z=13&ie=UTF8&iwloc=&output=embed')),
                ('fb', models.URLField(default='https://www.facebook.com', verbose_name='Facebook')),
                ('ig', models.URLField(default='https://www.instagram.com/', verbose_name='Instagram')),
                ('tw', models.URLField(default='https://www.twitter.com/', verbose_name='Twitter')),
                ('pinterest', models.URLField(default='https://www.pinterest.com/', verbose_name='Pinterest')),
            ],
        ),
    ]
