# Generated by Django 5.0 on 2023-12-15 20:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0006_alter_verificationcodetypemodel_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='verificationcodemodel',
            options={'verbose_name': 'verification code', 'verbose_name_plural': 'verification codes'},
        ),
        migrations.AlterField(
            model_name='verificationcodemodel',
            name='type',
            field=models.ForeignKey(help_text='User verification code type', on_delete=django.db.models.deletion.PROTECT, related_name='verification_code', to='security.verificationcodetypemodel', verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='verificationcodemodel',
            name='user',
            field=models.OneToOneField(help_text='User user', on_delete=django.db.models.deletion.PROTECT, related_name='verification_code', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterModelTable(
            name='verificationcodemodel',
            table='verification_code',
        ),
    ]
