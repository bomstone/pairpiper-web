from django.db import models

class PiperDatabase(models.Model):
    date = models.CharField(max_length=30, null=False)
    symbol = models.CharField(max_length=30, null=False)
    opening_price = models.DecimalField(max_digits=10, decimal_places=3, null=False)
    high_price = models.DecimalField(max_digits=10, decimal_places=3, null=False)
    low_price = models.DecimalField(max_digits=10, decimal_places=3, null=False)
    closing_price = models.DecimalField(max_digits=10, decimal_places=3, null=False)
    timestamp = models.CharField(max_length=50, null=True)


    class Meta():
        db_table = 'piperdb'

    def __unicode__(self):
        return '%s %s %s %s %s %s %s' % (
            self.date,
            self.symbol,
            self.opening_price,
            self.high_price,
            self.low_price,
            self.closing_price,
            self.timestamp
            )
