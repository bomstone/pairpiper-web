# Generated by Django 2.1.5 on 2019-01-22 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piperdatabase', '0002_auto_20190123_0016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='piperdatabase',
            old_name='close_price',
            new_name='closing_price',
        ),
        migrations.RenameField(
            model_name='piperdatabase',
            old_name='open_price',
            new_name='opening_price',
        ),
    ]