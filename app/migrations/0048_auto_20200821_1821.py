# Generated by Django 2.2.11 on 2020-08-21 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0047_auto_20200821_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectactivemq',
            name='instance',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='app.ActivemqInstance'),
        ),
        migrations.AlterField(
            model_name='projectrabbitmq',
            name='instance',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='app.RabbitmqInstance'),
        ),
        migrations.AlterField(
            model_name='projectredis',
            name='instance',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='app.RedisInstance'),
        ),
        migrations.AlterField(
            model_name='projectzookeeper',
            name='instance',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='app.ZookeeperInstance'),
        ),
    ]
