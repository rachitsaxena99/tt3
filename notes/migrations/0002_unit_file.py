# Generated by Django 3.2.12 on 2022-05-11 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]