# Generated by Django 5.0.1 on 2024-03-05 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("vehicles", "0022_alter_vehicle_brand_alter_vehicle_owner"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="vehicle",
            unique_together=set(),
        ),
    ]
