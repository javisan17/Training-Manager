# Generated by Django 5.1.6 on 2025-03-31 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tma", "0005_zones_delete_mesociclos_goals_description_goals_user_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="goals",
            name="description",
        ),
        migrations.RemoveField(
            model_name="goals",
            name="type",
        ),
    ]
