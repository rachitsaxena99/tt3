# Generated by Django 3.2.12 on 2022-05-09 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220509_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='connections',
        ),
    ]
