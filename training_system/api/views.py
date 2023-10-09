from django.shortcuts import render
from training_system.api.models import Product, User, Lesson, LessonViews, ProductAccess
from rest_framework import viewsets
from training_system.api.serializers import ProductSerializer, LessonSerializer, UserSerializer, LessonViewsSerializer, ProductAccessSerializer

# Create your views here.
class LessonViewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LessonViews.objects.all()
    serializer_class = LessonViewsSerializer