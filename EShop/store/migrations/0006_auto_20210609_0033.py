# Generated by Django 3.1.7 on 2021-06-08 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
