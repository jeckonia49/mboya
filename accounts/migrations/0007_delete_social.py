# Generated by Django 4.2.5 on 2023-09-06 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_profile_first_name_profile_last_name"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Social",
        ),
    ]
