from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from apis.models import Student, Subject
from apis.serializers import Student_serializer, Subject_serializer


@api_view(['GET'])
def student(request):
    students = Student.objects.all()
    serializer = Student_serializer(students, many = True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def subject(request):
    subjects = Subject.objects.all()
    serializer = Subject_serializer(subjects, many = True)

    return Response(serializer.data, status=status.HTTP_200_OK)
