from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_program = models.CharField(max_length=100)


class Subject(models.Model):
    subject_title = models.CharField(max_length=100)
    yos = models.IntegerField()
    semester = models.IntegerField()