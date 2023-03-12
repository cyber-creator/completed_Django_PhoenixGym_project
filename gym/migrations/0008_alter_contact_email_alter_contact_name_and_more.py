# Generated by Django 4.1.2 on 2022-12-01 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0007_contact_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]