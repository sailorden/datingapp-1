# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-09 06:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ExtUser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extuser',
            name='join_date',
        ),
        migrations.AddField(
            model_name='extuser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='extuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='extuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='last name'),
        ),
    ]
