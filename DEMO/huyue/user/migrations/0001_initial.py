# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-04-10 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, verbose_name='名称')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='价格')),
                ('count', models.IntegerField(default=0, verbose_name='数量')),
            ],
        ),
    ]
