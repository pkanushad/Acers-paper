# Generated by Django 4.1.5 on 2023-03-27 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_futureblottermodel_delete_futuresblottersmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='futureblottermodel',
            name='clearer',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
