# Generated by Django 2.0.7 on 2018-08-01 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20180801_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]