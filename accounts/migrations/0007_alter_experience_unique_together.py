# Generated by Django 3.2.12 on 2022-05-12 14:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0006_profile_skills'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='experience',
            unique_together={('user', 'startDate')},
        ),
    ]
