# Generated by Django 2.2.5 on 2019-09-10 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
