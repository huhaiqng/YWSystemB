# Generated by Django 2.2.11 on 2020-10-22 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0055_projectcodeaddr'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='software',
            options={'verbose_name': '项目组件', 'verbose_name_plural': '项目组件'},
        ),
        migrations.AlterField(
            model_name='software',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='名称'),
        ),
    ]
