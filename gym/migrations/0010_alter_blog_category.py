# Generated by Django 4.1.2 on 2023-01-11 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0009_blog_blog_text_next'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='gym.blogcategory'),
        ),
    ]
