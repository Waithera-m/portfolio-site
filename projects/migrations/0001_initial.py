# Generated by Django 3.0.6 on 2020-05-21 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=70)),
                ('description', models.TextField(max_length=300)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
    ]
