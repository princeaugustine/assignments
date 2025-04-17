from rest_framework import serializers

from apis.models import Student, Subject

class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_name', 'student_program']

class Subject_serializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['subject_title', 'yos', 'semester']