# Generated by Django 2.0.7 on 2018-08-01 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(max_length=10),
        ),
    ]
