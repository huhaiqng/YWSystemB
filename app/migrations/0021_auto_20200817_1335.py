# Generated by Django 2.2.11 on 2020-08-17 05:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20200817_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmysqldb',
            name='addr',
            field=models.CharField(blank=True, max_length=200, verbose_name='地址'),
        ),
        migrations.AddField(
            model_name='projectmysqldb',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='projectmysqldb',
            name='dir',
            field=models.CharField(blank=True, max_length=200, verbose_name='路径'),
        ),
        migrations.AddField(
            model_name='projectmysqldb',
            name='env',
            field=models.CharField(blank=True, max_length=200, verbose_name='环境'),
        ),
        migrations.AddField(
            model_name='projectmysqldb',
            name='method',
            field=models.CharField(default='normal', max_length=200, verbose_name='部署方式'),
        ),
        migrations.AddField(
            model_name='projectmysqldb',
            name='password',
            field=models.CharField(blank=True, max_length=200, verbose_name='密码'),
        ),
        migrations.AddField(
            model_name='projectmysqldb',
            name='port',
            field=models.CharField(blank=True, max_length=200, verbose_name='端口号'),
        ),
        migrations.AddField(
            model_name='projectmysqldb',
            name='project',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='app.Project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectmysqldb',
            name='role',
            field=models.CharField(blank=True, max_length=200, verbose_name='角色'),
        ),
        migrations.AddField(
            model_name='projectmysqldb',
            name='username',
            field=models.CharField(blank=True, max_length=200, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='projectmysqldb',
            name='name',
            field=models.CharField(blank=True, max_length=200, verbose_name='数据库名'),
        ),
    ]
