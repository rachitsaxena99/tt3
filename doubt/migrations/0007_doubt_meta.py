# Generated by Django 3.2.12 on 2022-05-12 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doubt', '0006_doubt_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='doubt',
            name='meta',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
