# Generated by Django 2.2.4 on 2019-08-21 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeFrom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='tng',
            options={'ordering': ['-date_pub']},
        ),
        migrations.RemoveField(
            model_name='tng',
            name='age_up',
        ),
        migrations.AlterField(
            model_name='tng',
            name='age_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.AgeFrom', verbose_name='Со скольки лет:'),
        ),
        migrations.AlterField(
            model_name='tng',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
