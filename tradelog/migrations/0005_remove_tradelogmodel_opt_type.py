# Generated by Django 2.1.5 on 2019-02-07 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tradelog', '0004_auto_20190206_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tradelogmodel',
            name='opt_type',
        ),
    ]