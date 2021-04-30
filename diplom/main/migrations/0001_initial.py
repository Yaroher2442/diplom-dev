# Generated by Django 3.2 on 2021-04-29 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descr', models.CharField(max_length=200)),
                ('create_time', models.DateTimeField()),
                ('change_time', models.DateTimeField()),
                ('executor', models.CharField(max_length=200)),
                ('owner', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Funnels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('descr', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descr', models.CharField(max_length=200)),
                ('create_time', models.DateTimeField()),
                ('change_time', models.DateTimeField()),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cases')),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('descr', models.CharField(max_length=200)),
                ('create_time', models.DateTimeField()),
                ('change_time', models.DateTimeField()),
                ('funnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.funnels')),
            ],
        ),
        migrations.AddField(
            model_name='cases',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.clients'),
        ),
        migrations.AddField(
            model_name='cases',
            name='funnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.funnels'),
        ),
    ]
