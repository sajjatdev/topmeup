from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


{

    "call_log": "1",
    "sponsor_number": "1",
    "user_number": "22",
    "network": "33",
    "amount": "3"
}


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

            return Response({"User Number": user_number, "Sponsor Number": sponsor_number, "amount": amount, "url": "https://paymentLink.com/pay/", }, status.HTTP_200_OK)

    def get(self, request, format=None):
        return Response({"status": "get request Success"})


def paymentPage(request):
    content = {
        "BaseURL": "https://instapay-sandbox.trustlinkhosting.com",
        "amount": "12.00",
        "sponsor_number": "1",
        "user_number": "22",
        "network": "33",
    }
    return render(request, 'payment.html', context=content)
