# Generated by Django 4.2.6 on 2024-01-06 16:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("xeroxapp", "0019_ownerorder"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Credentials",
            new_name="StudentCredentials",
        ),
    ]
