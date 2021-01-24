# Generated by Django 3.1.2 on 2021-01-23 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210123_1048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_city',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_phone_number',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_postcode',
            new_name='postcode',
        ),
    ]