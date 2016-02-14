# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_name', models.CharField(max_length=50)),
                ('borrowed_date', models.DateField(default=datetime.datetime(2016, 2, 11, 16, 5, 34, 451243, tzinfo=utc))),
                ('Lend_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_date', models.DateField(default=datetime.datetime(2016, 2, 11, 16, 5, 34, 451243, tzinfo=utc))),
                ('equipment', models.ForeignKey(to='system.Equipment')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reserved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserved', models.DateField(default=datetime.datetime(2016, 2, 11, 16, 5, 34, 451243, tzinfo=utc))),
                ('equipment', models.ForeignKey(to='system.Equipment')),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_data', models.CharField(max_length=50)),
                ('equipment_name', models.ForeignKey(to='system.Equipment')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_id', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.ForeignKey(to='system.Request')),
                ('user', models.ForeignKey(to='system.User')),
            ],
        ),
        migrations.AddField(
            model_name='reserved',
            name='user',
            field=models.ForeignKey(to='system.User'),
        ),
        migrations.AddField(
            model_name='log',
            name='user',
            field=models.ForeignKey(to='system.User'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='borrower',
            field=models.ForeignKey(to='system.User'),
        ),
    ]
