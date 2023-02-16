from django.contrib import admin
from .models import USSD


class PaymentRequest(admin.ModelAdmin):
    list_display = ('sponsor_number', 'user_number',
                    'network', 'amount', 'status',)


admin.site.register(USSD, PaymentRequest)
