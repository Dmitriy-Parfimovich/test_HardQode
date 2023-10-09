from training_system.api.models import Product, User, Lesson, ProductAccess, LessonViews
from rest_framework import serializers

class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'video_link', 'duration']

class LessonViewsSerializer(serializers.HyperlinkedModelSerializer):
    lessons = LessonSerializer(many=True)
    class Meta:
        model = LessonViews
        fields = ['lessons', 'view_duration', 'view_status']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    lessons = LessonSerializer(many=True)
    class Meta:
        model = Product
        fields = ['title', 'owner', 'lessons']

class ProductAccessSerializer(serializers.HyperlinkedModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = ProductAccess
        fields = ['products', 'user_access']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    views = LessonViewsSerializer(many=True)
    product_accesses = ProductAccessSerializer(many=True)
    class Meta:
        model = User
        fields = ['name', 'views', 'product_accesses']



