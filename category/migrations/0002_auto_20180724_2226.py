# Generated by Django 2.0.7 on 2018-07-24 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
    ]
