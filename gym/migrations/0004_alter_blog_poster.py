# Generated by Django 4.1.2 on 2022-11-26 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0003_blog_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='poster',
            field=models.ImageField(default='img/blog/news/news_1.jpg', null=True, upload_to='poster/', verbose_name='Poster'),
        ),
    ]