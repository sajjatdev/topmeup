import random
import string
from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import USSD

{

    "call_log": "1",
    "sponsor_number": "1",
    "user_number": "22",
    "network": "33",
    "amount": "3"
}


def random_string_generator(size=10, chars=string.ascii_lowercase+string.digits):
    return "".join(random.choice(chars) for _ in range(size))


class Index(APIView):

    def post(self, request, format=None):

        call_log = request.data.get("call_log")
        sponsor_number = request.data.get("sponsor_number")
        user_number = request.data.get("user_number")
        network = request.data.get("network")
        amount = request.data.get("amount")

        if call_log is None:
            return Response({"Error Message": "Call Log NO Required"}, status.HTTP_404_NOT_FOUND)
        elif sponsor_number is None:
            return Response({"Error Message": "Sponsor Number Required"}, status.HTTP_404_NOT_FOUND)
        elif user_number is None:
            return Response({"Error Message": "User Number Required"}, status.HTTP_404_NOT_FOUND)
        elif network is None:
            return Response({"Error Message": "Network Required"}, status.HTTP_404_NOT_FOUND)
        elif amount is None:
            return Response({"Error Message": "Amount Required"}, status.HTTP_404_NOT_FOUND)
        else:
            token = random_string_generator()

            USSD.objects.create(id=token, call_log=call_log, sponsor_number=sponsor_number,
                                user_number=user_number, network=network, amount=amount, status="padding")
            return Response({"User Number": user_number, "Sponsor Number": sponsor_number, "amount": amount, "url": "http://35.195.159.202:5000/payment/request/?token="+token, }, status.HTTP_200_OK)

    def get(self, request, format=None):
        return Response({"status": "get request Success"})


def paymentPage(request):

    token = request.GET.get("token")
    if not token is None:
        data = USSD.objects.get(id=token)
        content = {
            "BaseURL": "https://instapay-live.trustlinkhosting.com",
            "amount": data.amount,
            "sponsor_number": data.sponsor_number,
            "user_number": data.user_number,
            "network": data.network,
            "datetime": data.create_at
        }
        return render(request, 'payment.html', context=content)
    else:
        return render(request, 'notfound.html')
