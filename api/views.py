from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Students
from .serializers import StudentSerializer
from api import serializers

# Create your views here.


@api_view(['GET'])
def apis(request):
    apis = {
        'stud-create/': 'stud-create',
        'stud-list/': 'stud-create',
        'stud-update/<int:pk>/': 'stud-create',
        'stud-delete/<int:pk>/': 'stud-create',
    }
    return Response(apis)


@api_view(['GET'])
def studentList(request):
    students = Students.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def studentCreate(request):
    studSlz = StudentSerializer(data=request.data)
    if studSlz.is_valid():
        studSlz.save()
    return Response("Student added successfully")


@api_view(['POST'])
def studentUpdate(request, pk):
    student = Students.objects.get(id=pk)
    studSlz = StudentSerializer(instance=student, data=request.data)
    if studSlz.is_valid():
        studSlz.save()
    return Response("Updated sussessfully")


@api_view(['DELETE'])
def studentDelete(request, pk):
    student = Students.objects.get(id=pk)
    student.delete()
    return Response("Deleted successfully")
