# Generated by Django 4.2.4 on 2023-08-11 18:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_profile_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="is_public",
            field=models.BooleanField(default=False),
        ),
    ]
