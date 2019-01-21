# Generated by Django 2.1.5 on 2019-01-21 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliopart',
            name='close_date',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='portfoliopart',
            name='close_time',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='portfoliopart',
            name='currency',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=10),
        ),
        migrations.AddField(
            model_name='portfoliopart',
            name='fx_close',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=10),
        ),
        migrations.AddField(
            model_name='portfoliopart',
            name='fx_open',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=10),
        ),
        migrations.AddField(
            model_name='portfoliopart',
            name='net_close_sek',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=10),
        ),
        migrations.AddField(
            model_name='portfoliopart',
            name='net_open_sek',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=10),
        ),
        migrations.AddField(
            model_name='portfoliopart',
            name='net_result_sek',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=10),
        ),
        migrations.AddField(
            model_name='portfoliopart',
            name='opt_date',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='portfoliopart',
            name='opt_strie',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=10),
        ),
        migrations.AddField(
            model_name='portfoliopart',
            name='opt_type',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='portfoliopart',
            name='trade_type',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='portfoliopart',
            name='ul_close',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=10),
        ),
        migrations.AddField(
            model_name='portfoliopart',
            name='user',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='portfoliopart',
            name='asset',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='portfoliopart',
            name='commission',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=10),
        ),
        migrations.AlterField(
            model_name='portfoliopart',
            name='mf_finlevel',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=10),
        ),
        migrations.AlterField(
            model_name='portfoliopart',
            name='open_date',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='portfoliopart',
            name='open_price',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=10),
        ),
        migrations.AlterField(
            model_name='portfoliopart',
            name='open_time',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='portfoliopart',
            name='product_type',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='portfoliopart',
            name='quantity',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='portfoliopart',
            name='strategy',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='portfoliopart',
            name='trade_id',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='portfoliopart',
            name='true_exposure',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=10),
        ),
        migrations.AlterField(
            model_name='portfoliopart',
            name='ul_open',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=10),
        ),
    ]
