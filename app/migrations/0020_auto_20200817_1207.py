# Generated by Django 2.2.11 on 2020-08-17 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20200817_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectmysqldb',
            name='addr',
        ),
        migrations.RemoveField(
            model_name='projectmysqldb',
            name='created',
        ),
        migrations.RemoveField(
            model_name='projectmysqldb',
            name='data_dir',
        ),
        migrations.RemoveField(
            model_name='projectmysqldb',
            name='env',
        ),
        migrations.RemoveField(
            model_name='projectmysqldb',
            name='port',
        ),
        migrations.RemoveField(
            model_name='projectmysqldb',
            name='role',
        ),
        migrations.RemoveField(
            model_name='projectmysqldb',
            name='root_password',
        ),
        migrations.RemoveField(
            model_name='projectmysqldb',
            name='version',
        ),
    ]
