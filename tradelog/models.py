from django.db import models


class TradelogModel(models.Model):
    trade_id = models.IntegerField(default=None, null=True, blank=True)
    insert_type = models.CharField(max_length=30, default=None, null=True, blank=True)
    strategy = models.CharField(max_length=30, default=None, null=True, blank=True)
    product_type = models.CharField(max_length=30, default=None, null=True, blank=True)
    asset = models.CharField(max_length=30, default=None, null=True, blank=True)
    currency = models.CharField(max_length=4, default='SEK', null=True, blank=True)
    open_date = models.CharField(max_length=30, default=None, null=True, blank=True)
    open_time = models.CharField(max_length=30, default=None, null=True, blank=True)
    open_price = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True, blank=True)
    ul_open = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True, blank=True)
    true_exposure = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True, blank=True)
    fx_open = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True, blank=True)
    net_open_sek = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True, blank=True)
    quantity = models.IntegerField(default=None, null=True, blank=True)
    close_date = models.CharField(max_length=30, default=None, null=True, blank=True)
    close_time = models.CharField(max_length=30, default=None, null=True, blank=True)
    close_price = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True, blank=True)
    ul_close = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True, blank=True)
    fx_close = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True, blank=True)
    net_close_sek = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True, blank=True)
    commission = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True, blank=True)
    net_result_sek = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True, blank=True)
    mf_finlevel = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True, blank=True)
    opt_date = models.CharField(max_length=30, default=None, null=True, blank=True)
    opt_strike = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True, blank=True)
    user = models.CharField(max_length=30, default=None, null=True, blank=True)

    class Meta():
        db_table = 'tradelog'

    def __unicode__(self):
        return '%s %s %s %s %s %s %s %s %s' % (
            self.trade_id,
            self.insert_type,
            self.strategy,
            self.open_date,
            self.product_type,
            self.asset,
            self.close_date,
            self.net_result_sek,
            self.user,
            )
