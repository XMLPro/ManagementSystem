# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
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
                ('borrowed_date', models.DateField(default=datetime.date(2016, 2, 4))),
                ('Lend_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LendingHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_date', models.DateField(default=datetime.date(2016, 2, 4))),
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
            name='Users',
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
                ('user', models.ForeignKey(to='system.Users')),
            ],
        ),
        migrations.AddField(
            model_name='reserved',
            name='user',
            field=models.ForeignKey(to='system.Users'),
        ),
        migrations.AddField(
            model_name='lendinghistory',
            name='user',
            field=models.ForeignKey(to='system.Users'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='borrower',
            field=models.ForeignKey(to='system.Users'),
        ),
    ]
