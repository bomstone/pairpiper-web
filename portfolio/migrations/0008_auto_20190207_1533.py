# Generated by Django 2.1.5 on 2019-02-07 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20190207_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliomodel',
            name='open_date',
            field=models.CharField(default=None, max_length=30),
        ),
    ]