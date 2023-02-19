from django.contrib import admin
from .models import USSD


class PaymentRequest(admin.ModelAdmin):
    list_display = ("id", 'sponsor_number', 'user_number',
                    'network', 'amount', "create_at", 'status',)


admin.site.register(USSD, PaymentRequest)
