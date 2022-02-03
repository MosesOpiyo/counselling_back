# Generated by Django 3.2.9 on 2022-02-03 14:40

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counsel_users', '0005_alter_account_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
    ]