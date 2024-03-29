# Generated by Django 4.2.9 on 2024-01-09 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AboutUs",
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
                ("text", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
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
                ("address", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=15)),
                ("account_number", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("registration_number", models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Feedback",
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
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("phone_number", models.CharField(max_length=15)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("text", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Merchandise",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("available_quantity", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=255)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("text", models.TextField()),
                (
                    "video",
                    models.FileField(blank=True, null=True, upload_to="news/videos/"),
                ),
                ("photo1", models.ImageField(blank=True, upload_to="news/photos/")),
                ("photo2", models.ImageField(blank=True, upload_to="news/photos/")),
                ("photo3", models.ImageField(blank=True, upload_to="news/photos/")),
                ("photo4", models.ImageField(blank=True, upload_to="news/photos/")),
                ("photo5", models.ImageField(blank=True, upload_to="news/photos/")),
                ("photo6", models.ImageField(blank=True, upload_to="news/photos/")),
                ("photo7", models.ImageField(blank=True, upload_to="news/photos/")),
                ("photo8", models.ImageField(blank=True, upload_to="news/photos/")),
                ("photo9", models.ImageField(blank=True, upload_to="news/photos/")),
                ("photo10", models.ImageField(blank=True, upload_to="news/photos/")),
            ],
        ),
        migrations.CreateModel(
            name="Price",
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
                ("name", models.CharField(max_length=255)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Size",
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
                ("name", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Trainer",
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
                ("name", models.CharField(max_length=255)),
                ("photo", models.ImageField(upload_to="trainers/")),
                ("description", models.TextField()),
                ("is_available", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="TrainingRegistration",
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
                ("name", models.CharField(max_length=255)),
                ("age", models.PositiveIntegerField()),
                ("phone_number", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
                ("parent_name", models.CharField(max_length=255)),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("advanced", "Advanced"),
                            ("beginner", "Beginner"),
                            ("child", "Child"),
                        ],
                        default="beginner",
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MerchandisePhoto",
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
                ("photo", models.ImageField(upload_to="merchandise/")),
                (
                    "merchandise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.merchandise",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="merchandise",
            name="photos",
            field=models.ManyToManyField(
                blank=True,
                related_name="merchandise_photos",
                to="backend.merchandisephoto",
            ),
        ),
        migrations.AddField(
            model_name="merchandise",
            name="sizes",
            field=models.ManyToManyField(blank=True, to="backend.size"),
        ),
    ]
