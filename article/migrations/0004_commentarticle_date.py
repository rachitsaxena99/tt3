# Generated by Django 4.0.2 on 2022-04-28 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_alter_relationarticle_reaction_commentarticle'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentarticle',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
