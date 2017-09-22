# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 16:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_urls_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
