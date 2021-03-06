# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-17 23:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('description', models.TextField()),
                ('variables', models.TextField()),
                ('ask', models.TextField()),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Subjects')),
            ],
        ),
    ]
