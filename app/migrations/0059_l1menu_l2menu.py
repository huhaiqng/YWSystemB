# Generated by Django 2.2.11 on 2021-01-27 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0058_auto_20210127_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='L1Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='名称')),
                ('path', models.CharField(max_length=255, unique=True, verbose_name='URI')),
                ('component', models.CharField(default='Layout', max_length=255, verbose_name='部件')),
                ('redirect', models.CharField(help_text='一级节点点击定向到子节点 URI', max_length=255, verbose_name='定向')),
                ('title', models.CharField(max_length=255, verbose_name='显示名称')),
                ('icon', models.CharField(default='tree', max_length=255, verbose_name='菜单图标')),
            ],
        ),
        migrations.CreateModel(
            name='L2Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='名称')),
                ('path', models.CharField(default="() => import('@/views/')", max_length=255, unique=True, verbose_name='URI')),
                ('component', models.CharField(default='Layout', max_length=255, verbose_name='部件')),
                ('title', models.CharField(max_length=255, verbose_name='显示名称')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.L1Menu')),
            ],
        ),
    ]
