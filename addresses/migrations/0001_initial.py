# Generated by Django 2.0.7 on 2018-09-22 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('billing', '0002_auto_20180922_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=120)),
                ('address_line1', models.CharField(max_length=120)),
                ('address_line2', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('country', models.CharField(default='India', max_length=120)),
                ('postal_code', models.IntegerField(max_length=6)),
                ('billing_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.BillingProfile')),
            ],
        ),
    ]