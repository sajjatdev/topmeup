from django.db import models

# Create your models here.


class USSD(models.Model):

    # id = models.CharField(max_length=255)
    call_log = models.CharField(max_length=255)
    sponsor_number = models.CharField(max_length=255)
    user_number = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    # status = models.CharField(max_length=255)

    class Meta:

        verbose_name = 'USSD'
        verbose_name_plural = 'USSDs'

    def __str__(self):
        return self.call_log
