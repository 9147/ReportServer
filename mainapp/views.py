from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import  Class,UniqueGroupId,Device,Commit
from .serializers import ClassSerializer,DeviceSerializer
from .handler import checkAccountAccess
from django.utils import timezone

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
        # iterate throught the classes object
        for class_obj in classes:
            # check if the user has access to the class
            if not (checkAccountAccess(class_obj,request.user) or request.user.superuser):
                classes = classes.exclude(id=class_obj.id)
        # Serialize the data
        class_serializer = ClassSerializer(classes, many=True)
        # print(class_serializer)
        # Return the serialized data
        return Response({
            'access': 'Granted',
            'classes': class_serializer.data
        }, status=200)
    if req=='logout':
        # print(request)
        logout(request)
        return Response({'message': 'Successful logged out!'})
    if req=='access':
        # print(request.user)
        if request.user.is_authenticated:
            return Response({'access': 'Granted'}, status=200)
        else:
            return Response({'access': 'Denied'}, status=401)
    return Response({'error': 'Invalid request'}, status=400)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def live_api(request):
    req= request.data.get('request')
    if req=='live':
        ip = request.data.get('ipv6')
        device=Device.objects.get_or_create(device_ip=ip)[0]
        device.last_seen = timezone.now()
        device.save()
        try:
            for class_obj in Class.objects.all():
                if checkAccountAccess(class_obj,request.user) or request.user.superuser:
                    # print(class_obj)
                    uniquegroup=UniqueGroupId.objects.get(group_id=class_obj.group_id)
                    # print(uniquegroup)
                    # check if uniquegroup.group_devices has device
                    uniquegroup.save()
                    if not uniquegroup.group_devices.filter(device_ip=device.device_ip).exists():
                        uniquegroup.group_devices.add(device)
                    uniquegroup.save()
        except Exception as ex:
            # print(ex)
            return Response({'error': 'Invalid request'}, status=400)
        # print(req)
        return Response({'Successfull': 'Updated'}, status=200)
    elif req=='activedevices':
        pass
    return Response({'error':"Invalid request"},status=400)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_api(request):
    req = request.data.get('request')
    if req=='update':
        # print(request.data)
        class_name= request.data.get('class_name')
        section_no = request.data.get('section_no')
        adission_no = request.data.get('admission_no')
        print(class_name,section_no,adission_no)
        class_obj = Class.objects.get(name=class_name)
        print(class_obj)
        commit = Commit.objects.create(
            section_nos=section_no,
            admission_no=adission_no,
            commit_no=class_obj.commit_number+1
        )
        commit.save()
        class_obj.add_commit(commit)
        class_obj.commit_number+=1
        class_obj.save()
        # get all group devices
        devices=class_obj.group_id.group_devices.filter(last_seen__gte=timezone.now()-timezone.timedelta(minutes=5))
        devices_serializer=DeviceSerializer(devices,many=True)
        print(devices)
        return Response({'message': 'Updated successfully!','commit_no':class_obj.commit_number,'devices':devices_serializer.data}, status=200)
    else:
        return Response({'error': 'Invalid request'}, status=400)

