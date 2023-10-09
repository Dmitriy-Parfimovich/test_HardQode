from django.db import models


# Create your models here.
class Lesson(models.Model):
    title = models.CharField(max_length=200)
    video_link = models.CharField(max_length=200)
    duration = models.IntegerField()

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    owner = models.CharField(max_length=100)
    lessons = models.ManyToManyField(Lesson)

    def __str__(self):
        return self.title

class ProductAccess(models.Model):
    user_access = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class LessonViews(models.Model):
    lessons = models.ManyToManyField(Lesson)
    view_duration = models.IntegerField()

    def get_view_status(self):
        return 'viewed' if self.lesson.duration * 0.8 <= self.view_duration else 'not viewed'

    view_status = property(get_view_status)

class User(models.Model):
    name = models.CharField(max_length=100)
    views = models.ForeignKey(LessonViews, on_delete=models.CASCADE)
    product_accesses = models.ForeignKey(ProductAccess, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

