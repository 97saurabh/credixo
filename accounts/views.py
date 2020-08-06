from django.shortcuts import render


from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import RegisterSeri
from rest_framework.authtoken.models import Token



@api_view(['POST',])
def registration(request):
    if request.method == 'POST':

        serializer = RegisterSeri(data=request.data)
        data = {}
        if serializer.is_valid():

            account = serializer.save()
            token = Token.objects.get(user=account).key
            data['token'] = token
            data['response'] = "Successful Resgister new User"
        else:
            print(serializer.errors)
            data = serializer.errors
        return Response(data)
