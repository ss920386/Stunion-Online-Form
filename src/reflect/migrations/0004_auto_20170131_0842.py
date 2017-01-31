# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reflect', '0003_auto_20170131_0151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=500)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('reflectionID', models.IntegerField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='reflection',
            name='replies',
            field=models.ManyToManyField(to='reflect.Reply'),
        ),
    ]