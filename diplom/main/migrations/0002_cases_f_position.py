# Generated by Django 3.2 on 2021-04-29 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cases',
            name='f_position',
            field=models.IntegerField(default=0),
        ),
    ]
