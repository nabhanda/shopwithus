# Generated by Django 2.0.7 on 2018-08-02 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20180724_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
