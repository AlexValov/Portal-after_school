# Generated by Django 2.2 on 2019-06-29 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20190629_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tng',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
