# Generated by Django 4.2.16 on 2024-11-11 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0004_rename_phone_no_employee_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="password",
            field=models.CharField(default="employee@123", max_length=128),
        ),
    ]
