# Generated by Django 2.2.11 on 2020-08-22 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0048_auto_20200821_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectweb',
            name='file_dir',
            field=models.CharField(blank=True, max_length=200, verbose_name='文件路径'),
        ),
        migrations.AlterField(
            model_name='projectweb',
            name='dir',
            field=models.CharField(blank=True, max_length=200, verbose_name='安装路径'),
        ),
    ]
