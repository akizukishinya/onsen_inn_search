# Generated by Django 2.2.1 on 2019-06-01 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onsen_inns', '0005_auto_20190601_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onsen',
            name='onsen_address',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
