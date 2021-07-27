from django.shortcuts import redirect
from rest_framework import generics
from rest_framework import viewsets
from .import models
from .import serializers

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST




from .models import User,ServiceProvider
from .serializers import UserSerializer, UserLoginSerializer, UserLogoutSerializer,ServiceProviderSerializer,ServiceProviderTruckSerializer


class Record(generics.ListCreateAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Login(generics.GenericAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLoginSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


class Logout(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserLogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLogoutSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


class ServiceProviderViewset(generics.ListCreateAPIView):
    queryset = models.ServiceProvider.objects.all()
    serializer_class = serializers.ServiceProviderSerializer


class TruckViewset(generics.ListCreateAPIView):
    queryset = models.Trucks.objects.all()
    serializer_class = serializers.TruckSerializer


class OrderViewset(generics.ListCreateAPIView):
    queryset = models.Orders.objects.all()
    serializer_class = serializers.OrderSerializer


class ServiceProviderUserViewset(generics.ListCreateAPIView):
    queryset = models.ServiceProviderUser.objects.all()
    serializer_class = serializers.ServiceProviderUserSerializer



class ServiceProviderTruckViewset(generics.ListCreateAPIView):
    queryset = models.ServiceProviderTruck.objects.all()
    serializer_class = serializers.ServiceProviderTruckSerializer



def index(request):
    return redirect('/api/signup')