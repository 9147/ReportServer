from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def log(request):
    # get the ip address
    ip = request.META.get('REMOTE_ADDR')
    port= request.data.get('port')
    print(ip, port,request.META)
    return Response({'message': 'Logged in successfully!'}, status=200)

    
