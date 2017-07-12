# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-11 17:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0012_auto_20170629_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='pref_key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiments', to='projects.Project'),
        ),
    ]