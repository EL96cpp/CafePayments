from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Cafe, Employee
from django.contrib.auth import authenticate


class EmployeeLoginAPI(APIView):
    def post(self, request):
        print(request)
        name = request.data.get('name')
        surname = request.data.get('surname')
        password = request.data.get('password')
        user = authenticate(name=name, surname=surname, password=password)

        if user:
            return Response({'login': 'ok!'}, status=status.HTTP_200_OK)
        else:
            return Response({'login': 'incorrect data!'}, status=status.HTTP_401_UNAUTHORIZED)
