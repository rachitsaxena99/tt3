# Generated by Django 3.2.12 on 2022-05-11 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_subject_units'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
