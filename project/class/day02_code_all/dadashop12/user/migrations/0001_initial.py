# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-04-11 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=11, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('is_active', models.BooleanField(default=False, verbose_name='激活状态')),
            ],
            options={
                'db_table': 'user_user_profile',
            },
        ),
    ]