# Generated by Django 5.1.3 on 2024-11-27 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0002_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                default="default.jpg", upload_to="profile_pictures"
            ),
        ),
    ]
