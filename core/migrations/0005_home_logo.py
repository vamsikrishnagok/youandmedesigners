# Generated by Django 2.2 on 2019-04-28 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190428_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
