# Generated by Django 3.2.9 on 2022-02-01 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('councelapp', '0018_auto_20220201_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='councelapp.group'),
        ),
    ]
