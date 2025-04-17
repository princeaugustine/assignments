from django.urls import path
from apis import views

urlpatterns = [
    path('students/', views.student, name='student'),
    path('subjects/', views.subject, name='subject')
]