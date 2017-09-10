from django.contrib.auth.models import Group, User
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework.permissions import IsAdminUser


from .serializers import *
from .models import *

def index(request):
    return render(request, 'schoolapp/index.html', {})

# def create_student(request):

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, format=None):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


# 市场渠道管理
class MarketChannelList(generics.ListCreateAPIView):
    queryset = MarketChannel.objects.all()
    serializer_class = MarketChannelSerializer

    def create(self, request, format=None):
        queryset = self.get_queryset()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, format=None):
        serializer = MarketChannelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
    