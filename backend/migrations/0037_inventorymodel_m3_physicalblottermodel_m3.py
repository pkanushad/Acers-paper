# Generated by Django 4.1.5 on 2023-04-17 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0036_alter_inventorymodel_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorymodel',
            name='m3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='physicalblottermodel',
            name='m3',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
