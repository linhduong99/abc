from django.db import models
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.forms.models import model_to_dict
from .models import Student
from .serializers import StudentSerializer

class ListCreateStudentView(ListCreateAPIView):
    model = Student
    serializer_class = StudentSerializer
    
    def get(self, request):
        users = Student.objects.all()
        serializer = StudentSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
    def create(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
        

class GetStudentView(APIView):
    models = Student
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        get_user = Student.objects.get(id=kwargs.get('id'))
        serializer = StudentSerializer(get_user, many=False)
        if get_user is not None:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors , status = status.HTTP_404_NOT_FOUND)
    

        
