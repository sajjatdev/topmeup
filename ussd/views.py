from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class Index(APIView):
    def post(self, request, format=None):
        return Response({"Status": "success"})

    def get(self, request, format=None):
        return Response({"status": "get request Success"})
