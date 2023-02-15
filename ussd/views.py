from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Index(APIView):
    def post(self, request, format=None):
        call_log = request.POST.get("callog", None)
        sponsor_number = request.POST.get("sponsor_number", None)
        user_number = request.POST.get("user_number", None)
        network = request.POST.get("network", None)
        amount = request.POST.get("amount", None)

        return Response({"Sponsor Number": sponsor_number, "amount": amount, "url": "https://paymentLink.com/pay/", }, status.HTTP_200_OK)

    def get(self, request, format=None):
        return Response({"status": "get request Success"})
