# Generated by Django 4.1.2 on 2022-11-26 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profilecoach_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilecoach',
            name='avatar',
            field=models.ImageField(default='profile/default_profile.jpg', upload_to='avatar/'),
        ),
    ]