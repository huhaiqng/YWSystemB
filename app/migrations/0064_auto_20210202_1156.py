# Generated by Django 2.2.11 on 2021-02-02 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0063_auto_20210202_1144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='l1menu',
            options={'ordering': ['order'], 'verbose_name': '一级菜单', 'verbose_name_plural': '一级菜单'},
        ),
        migrations.AddField(
            model_name='l2menu',
            name='order',
            field=models.IntegerField(default=10, help_text='菜单排序，小的排前面', verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='l1menu',
            name='order',
            field=models.IntegerField(default=10, help_text='菜单排序，小的排前面', verbose_name='排序'),
        ),
    ]
