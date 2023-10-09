# Generated by Django 4.2.6 on 2023-10-09 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("video_link", models.CharField(max_length=200)),
                ("duration", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="LessonViews",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("view_duration", models.IntegerField()),
                ("lessons", models.ManyToManyField(to="api.lesson")),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("owner", models.CharField(max_length=100)),
                ("lessons", models.ManyToManyField(to="api.lesson")),
            ],
        ),
        migrations.CreateModel(
            name="ProductAccess",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_access", models.CharField(max_length=50)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.product"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "product_accesses",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.productaccess",
                    ),
                ),
                (
                    "views",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.lessonviews",
                    ),
                ),
            ],
        ),
    ]
