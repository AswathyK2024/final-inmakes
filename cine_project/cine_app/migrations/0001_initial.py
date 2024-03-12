# Generated by Django 4.2.11 on 2024-03-11 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100, unique=True)),
                ("slug", models.SlugField(max_length=150, unique=True)),
            ],
            options={
                "verbose_name": "category",
                "verbose_name_plural": "categories",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="MovieDetails",
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
                ("title", models.CharField(max_length=80)),
                ("slug", models.SlugField(max_length=150, unique=True)),
                ("poster", models.ImageField(blank=True, upload_to="moviedetails")),
                ("description", models.CharField(max_length=250)),
                ("release_date", models.DateField()),
                ("actors", models.CharField(max_length=250)),
                ("trailer_Link", models.CharField(blank=True, max_length=250)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cine_app.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "MovieDetail",
                "verbose_name_plural": "MovieDetails",
                "ordering": ("title",),
            },
        ),
        migrations.CreateModel(
            name="CommentSection",
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
                ("user", models.CharField(max_length=250)),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("message", models.CharField(max_length=250)),
                (
                    "movie_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="cine_app.moviedetails",
                    ),
                ),
            ],
            options={
                "verbose_name": "CommentSection",
                "verbose_name_plural": "CommentSections",
                "ordering": ("user",),
            },
        ),
    ]
