# Generated by Django 2.2.11 on 2020-08-11 03:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_projectjar_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectjar',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
    ]