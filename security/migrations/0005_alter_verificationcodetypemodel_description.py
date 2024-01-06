# Generated by Django 5.0 on 2023-12-15 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0004_verificationcodetypemodel_verificationcodemodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificationcodetypemodel',
            name='description',
            field=models.TextField(blank=True, help_text='Verification code type description', max_length=512, null=True, verbose_name='description'),
        ),
    ]