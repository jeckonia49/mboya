# Generated by Django 4.2.5 on 2023-09-06 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
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
                ("email", models.CharField(max_length=100)),
                ("phone", models.IntegerField()),
                ("message", models.TextField(max_length=300)),
            ],
        ),
    ]
