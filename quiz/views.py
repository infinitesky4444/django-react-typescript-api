from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Lesson
from .serializers import LessonSerializer

class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer