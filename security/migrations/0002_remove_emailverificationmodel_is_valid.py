# Generated by Django 5.0 on 2023-12-14 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailverificationmodel',
            name='is_valid',
        ),
    ]