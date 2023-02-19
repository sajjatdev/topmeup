from django.db import models

# Create your models here.


class USSD(models.Model):
    STATUS = [("padding", "Padding"), ("completed",
                                       "Completed"), ("failure", "Failure"), ("expire", "Expire")]
    id = models.CharField(max_length=255, primary_key=True)
    call_log = models.CharField(max_length=255)
    sponsor_number = models.CharField(max_length=255)
    user_number = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    status = models.CharField(max_length=255, choices=STATUS, default="None")
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = 'Payment Request'
        verbose_name_plural = 'Payment Request'

    def __str__(self):
        return self.sponsor_number
