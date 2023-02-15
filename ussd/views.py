from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Index(APIView):

    def post(self, request, format=None):

        call_log = request.data.get("call_log")
        sponsor_number = request.data.get("sponsor_number")
        user_number = request.data.get("user_number")
        network = request.data.get("network")
        amount = request.data.get("amount")

        if call_log is None:
            return Response({"Error Message": "Call Log NO Required"})
        elif sponsor_number is None:
            return Response({"Error Message": "Sponsor Number Required"})
        elif user_number is None:
            return Response({"Error Message": "User Number Required"})
        elif network is None:
            return Response({"Error Message": "Network Required"})
        elif amount is None:
            return Response({"Error Message": "Amount Required"})
        else:
            return Response({"Sponsor Number": sponsor_number, "amount": amount, "url": "https://paymentLink.com/pay/", }, status.HTTP_200_OK)

    def get(self, request, format=None):
        return Response({"status": "get request Success"})
