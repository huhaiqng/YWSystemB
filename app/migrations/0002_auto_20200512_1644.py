# Generated by Django 2.2.11 on 2020-05-12 08:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=200, verbose_name='密码')),
                ('addr', models.CharField(blank=True, max_length=200, null=True, verbose_name='地址')),
                ('use', models.CharField(max_length=255, verbose_name='用途')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='Env',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='环境名称')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='主机名')),
                ('ip', models.GenericIPAddressField(unique=True, verbose_name='IP 地址')),
                ('version', models.CharField(max_length=200, verbose_name='版本')),
                ('cpu', models.IntegerField(default=4, verbose_name='CPU 核数')),
                ('memory', models.CharField(default='8G', max_length=10, verbose_name='内存大小')),
                ('disk', models.CharField(default='80G', max_length=10, verbose_name='硬盘大小')),
                ('position', models.CharField(max_length=200, verbose_name='位置')),
                ('admin', models.CharField(default='root', max_length=200, verbose_name='系统管理员')),
                ('password', models.CharField(max_length=200, verbose_name='密码')),
                ('type', models.CharField(max_length=200, verbose_name='类别')),
                ('env', models.CharField(default='test', max_length=200, verbose_name='环境')),
                ('ins_num', models.IntegerField(default='0', verbose_name='实例数量')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='项目名称')),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='软件名称')),
                ('type', models.CharField(choices=[('general', 'general'), ('special', 'special')], default='general', max_length=200, verbose_name='类型')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='名称')),
                ('script_dir', models.CharField(max_length=200, verbose_name='脚本路径')),
                ('script_name', models.CharField(max_length=200, unique=True, verbose_name='脚本名')),
                ('arg', models.CharField(blank=True, max_length=200, verbose_name='参数')),
                ('type', models.CharField(max_length=200, verbose_name='类别')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectWeb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_ip', models.GenericIPAddressField(verbose_name='公网 IP')),
                ('domain', models.CharField(max_length=200, verbose_name='域名')),
                ('url', models.CharField(max_length=200, verbose_name='访问地址')),
                ('env', models.CharField(max_length=200, verbose_name='环境')),
                ('software', models.CharField(max_length=200, verbose_name='软件')),
                ('use', models.CharField(max_length=200, verbose_name='用途')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('host', models.ManyToManyField(to='app.Host')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='software',
            field=models.ManyToManyField(to='app.Software'),
        ),
        migrations.CreateModel(
            name='MySQLDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='数据库名')),
                ('username', models.CharField(max_length=200, verbose_name='用户名')),
                ('pro_password', models.CharField(max_length=200, verbose_name='测试环境密码')),
                ('test_password', models.CharField(max_length=200, verbose_name='生产环境密码')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Project')),
            ],
        ),
        migrations.CreateModel(
            name='JavaPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='包名')),
                ('port', models.IntegerField(verbose_name='端口号')),
                ('deploy_dir', models.CharField(max_length=200, verbose_name='部署路径')),
                ('download_addr', models.CharField(max_length=200, verbose_name='下载地址')),
                ('func', models.CharField(max_length=200, verbose_name='功能')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='java_package', to='app.Project')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProjectTomcat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=200, verbose_name='包名')),
                ('env', models.CharField(max_length=200, verbose_name='环境')),
                ('project', models.CharField(max_length=200, verbose_name='项目')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Host')),
            ],
            options={
                'unique_together': {('package_name', 'env', 'project', 'host')},
            },
        ),
        migrations.CreateModel(
            name='ProjectOracle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('env', models.CharField(max_length=200, verbose_name='环境')),
                ('type', models.CharField(max_length=200, verbose_name='类别')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Host')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Project')),
            ],
            options={
                'unique_together': {('env', 'project', 'host', 'type')},
            },
        ),
        migrations.CreateModel(
            name='ProjectMySQLDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('env', models.CharField(max_length=200, verbose_name='环境')),
                ('version', models.CharField(default='MySQL 5.7', max_length=200, verbose_name='版本')),
                ('port', models.IntegerField(default=3306)),
                ('role', models.CharField(max_length=200, verbose_name='角色')),
                ('root_password', models.CharField(max_length=200, verbose_name='ROOT 密码')),
                ('data_dir', models.CharField(max_length=200, verbose_name='数据目录')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Host')),
                ('mysqldb', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project_mysql', to='app.MySQLDB')),
            ],
            options={
                'unique_together': {('mysqldb', 'host')},
            },
        ),
        migrations.CreateModel(
            name='ProjectMongoDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('env', models.CharField(max_length=200, verbose_name='环境')),
                ('type', models.CharField(max_length=200, verbose_name='类别')),
                ('shard', models.CharField(blank=True, max_length=200, verbose_name='分片')),
                ('role', models.CharField(blank=True, max_length=200, verbose_name='角色')),
                ('port', models.IntegerField(blank=True, verbose_name='端口号')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Host')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Project')),
            ],
            options={
                'unique_together': {('env', 'project', 'host', 'port')},
            },
        ),
        migrations.CreateModel(
            name='ProjectGeneralSoftware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('env', models.CharField(max_length=200, verbose_name='环境')),
                ('software', models.CharField(max_length=200, verbose_name='软件')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Host')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Project')),
            ],
            options={
                'unique_together': {('env', 'project', 'host')},
            },
        ),
    ]