# Generated by Django 3.2.12 on 2022-05-30 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testroom', '0004_test_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='output',
            field=models.TextField(blank=True, null=True),
        ),
    ]
