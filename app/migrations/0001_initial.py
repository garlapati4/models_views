# Generated by Django 4.2.1 on 2023-06-20 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('topic_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.topic')),
            ],
        ),
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('date', models.IntegerField()),
                ('author', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.webpage')),
            ],
        ),
    ]
