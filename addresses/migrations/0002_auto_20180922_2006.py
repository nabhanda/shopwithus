# Generated by Django 2.0.7 on 2018-09-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.CharField(max_length=6),
        ),
    ]