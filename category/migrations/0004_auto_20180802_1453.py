# Generated by Django 2.0.7 on 2018-08-02 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_subcategory_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField(default=0)),
                ('stock', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='category.Category')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='category.Subcategory')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug')},
        ),
    ]