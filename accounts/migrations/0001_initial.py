# Generated by Django 4.1.2 on 2022-10-29 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileCoach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=250)),
                ('phone_number', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('gym_location', models.CharField(blank=True, max_length=250, null=True)),
                ('postal_code', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=250, null=True)),
                ('state', models.CharField(blank=True, max_length=250, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]