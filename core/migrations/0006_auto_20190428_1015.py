# Generated by Django 2.2 on 2019-04-28 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_home_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='services_desc_large',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='work_desc_large',
            field=models.TextField(blank=True, null=True),
        ),
    ]
