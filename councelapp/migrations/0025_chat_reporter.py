# Generated by Django 3.2.9 on 2022-02-01 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('councelapp', '0024_auto_20220201_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='reporter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]