# Generated by Django 2.2.11 on 2021-02-02 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0066_auto_20210202_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='l2menu',
            name='is_model',
            field=models.BooleanField(default=True, verbose_name='是否对应明细'),
        ),
    ]