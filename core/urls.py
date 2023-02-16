from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ussd.views import Index, paymentPage
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name="ussd"),
    path('payment/request/', paymentPage, name="paymentPage")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
