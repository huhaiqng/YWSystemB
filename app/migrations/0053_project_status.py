# Generated by Django 2.2.11 on 2020-10-21 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0052_auto_20200901_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(default='使用中', max_length=200, verbose_name='状态'),
        ),
    ]
