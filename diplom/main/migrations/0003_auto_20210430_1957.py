# Generated by Django 3.2 on 2021-04-30 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_cases_f_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='cases',
            name='stage',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tasks',
            name='status',
            field=models.CharField(default='', max_length=200),
        ),
    ]
