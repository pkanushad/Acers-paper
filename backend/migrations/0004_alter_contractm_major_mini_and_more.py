# Generated by Django 4.1.5 on 2023-03-24 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_swapblottermodel_duplicate_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractm',
            name='major_mini',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contractm',
            name='major_mini_conn',
            field=models.TextField(blank=True, null=True),
        ),
    ]
