# Generated by Django 4.1.2 on 2022-11-26 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profilecoach_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilecoach',
            name='biography',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]