from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import ReportField, ReportPage, Class
from .serializers import ReportFieldSerializer, ReportPageSerializer, ClassSerializer

@api_view(['POST'])
def login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')
    print(username, password)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token':token.key, 'user': user.username, 'message': 'Logged in successfully!'}, status=200)
    else:
        return Response({'error': 'Invalid credentials'}, status=400)

def home(request):
    return render(request,'mainapp/home.html')

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def data_api(request):
    req = request.data.get('request')
    if req=='scheme':
        classes = Class.objects.all()

        # Serialize the data
        class_serializer = ClassSerializer(classes, many=True)
        print(class_serializer)
        # Return the serialized data
        return Response({
            'access': 'Granted',
            'classes': class_serializer.data
        }, status=200)
    if req=='logout':
        print(request)
        logout(request)
        return Response({'message': 'Successful logged out!'})
    if req=='access':
        print(request.user)
        if request.user.is_authenticated:
            return Response({'access': 'Granted'}, status=200)
        else:
            return Response({'access': 'Denied'}, status=401)
    return Response({'error': 'Invalid request'}, status=400)
