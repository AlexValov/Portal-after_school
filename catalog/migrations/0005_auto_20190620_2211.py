# Generated by Django 2.2 on 2019-06-20 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20190620_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tng',
            name='price',
            field=models.CharField(default=0, max_length=50, verbose_name='Цена:'),
        ),
    ]
