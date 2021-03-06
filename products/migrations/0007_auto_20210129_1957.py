# Generated by Django 3.1.2 on 2021-01-29 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210123_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='additionalImages',
            field=models.FileField(blank=True, default='', null=True, upload_to='products/additional'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, default='', null=True, upload_to='products/products'),
        ),
    ]
