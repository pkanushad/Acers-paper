# Generated by Django 4.1.5 on 2023-03-19 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_swapblottermodel_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='swapblottermodel',
            name='duplicate_id',
            field=models.CharField(default='none', max_length=100),
        ),
    ]
