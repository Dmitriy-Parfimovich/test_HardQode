from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    duration = models.IntegerField()
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200)
    lessons = models.ManyToManyField(Lesson, through='ViewStatus')
    products = models.ManyToManyField(Product, through='UserAccess')

    def __str__(self):
        return self.name


class ViewStatus(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    view_duration = models.IntegerField()

    def get_view_status(self):
        return 'viewed' if self.lessons.duration * 0.8 <= self.view_duration else 'not viewed'

    view_status = property(get_view_status)


class UserAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_access = models.CharField(max_length=200)
