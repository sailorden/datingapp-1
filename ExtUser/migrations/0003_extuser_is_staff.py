# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-10 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExtUser', '0002_auto_20160809_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='extuser',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
