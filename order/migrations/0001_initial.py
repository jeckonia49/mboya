# Generated by Django 4.2.5 on 2023-09-06 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0007_delete_social"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("full_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("phone", models.IntegerField(help_text="0745547751")),
                ("address", models.CharField(max_length=100)),
                (
                    "instructions",
                    models.TextField(blank=True, max_length=300, null=True),
                ),
                ("completed", models.BooleanField(default=False)),
                (
                    "pickup_date",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "delivery_date",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="order_profile",
                        to="accounts.profile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Order",
                "verbose_name_plural": "Orders",
            },
        ),
    ]
