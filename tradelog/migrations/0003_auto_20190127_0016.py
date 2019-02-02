# Generated by Django 2.1.5 on 2019-01-26 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradelog', '0002_auto_20190127_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradelogmodel',
            name='asset',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='close_date',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='close_time',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='commission',
            field=models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='currency',
            field=models.CharField(blank=True, default=None, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='fx_close',
            field=models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='fx_open',
            field=models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='insert_type',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='mf_finlevel',
            field=models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='net_close_sek',
            field=models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='net_open_sek',
            field=models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='net_result_sek',
            field=models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='open_date',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='open_price',
            field=models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='open_time',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='opt_date',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='opt_strike',
            field=models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='opt_type',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='product_type',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='quantity',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='strategy',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='trade_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='true_exposure',
            field=models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='ul_close',
            field=models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='ul_open',
            field=models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='tradelogmodel',
            name='user',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
    ]
