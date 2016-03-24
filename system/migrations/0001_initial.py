# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.contrib.auth.models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True,
                                        verbose_name='ID', auto_created=True)),
                ('password',
                 models.CharField(max_length=128, verbose_name='password')),
                ('last_login',
                 models.DateTimeField(blank=True, verbose_name='last login',
                                      null=True)),
                ('is_superuser', models.BooleanField(default=False,
                                                     verbose_name='superuser status',
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username',
                 models.CharField(max_length=30, error_messages={
                     'unique': 'A user with that username already exists.'},
                                  validators=[
                                      django.core.validators.RegexValidator(
                                          '^[\\w.@+-]+$',
                                          'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.',
                                          'invalid')],
                                  verbose_name='username',
                                  help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                  unique=True)),
                ('first_name',
                 models.CharField(max_length=30, verbose_name='first name',
                                  blank=True)),
                ('last_name',
                 models.CharField(max_length=30, verbose_name='last name',
                                  blank=True)),
                ('email', models.EmailField(max_length=254,
                                            verbose_name='email address',
                                            blank=True)),
                ('is_staff', models.BooleanField(default=False,
                                                 verbose_name='staff status',
                                                 help_text='Designates whether the user can log into this admin site.')),
                ('is_active',
                 models.BooleanField(default=True, verbose_name='active',
                                     help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined',
                 models.DateTimeField(default=django.utils.timezone.now,
                                      verbose_name='date joined')),
                ('is_valid', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(related_name='user_set',
                                                  related_query_name='user',
                                                  to='auth.Group',
                                                  verbose_name='groups',
                                                  help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  blank=True)),
                ('user_permissions',
                 models.ManyToManyField(related_name='user_set',
                                        related_query_name='user',
                                        to='auth.Permission',
                                        verbose_name='user permissions',
                                        help_text='Specific permissions for this user.',
                                        blank=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True,
                                        verbose_name='ID', auto_created=True)),
                ('equipment_name', models.CharField(max_length=50)),
                ('borrowed_date', models.DateField(auto_now=True)),
                ('Lend_count', models.IntegerField(default=0)),
                ('borrower',
                 models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True,
                                   blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True,
                                        verbose_name='ID', auto_created=True)),
                ('borrowed_date', models.DateField(auto_now=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('equipment', models.ForeignKey(to='system.Equipment')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True,
                                        verbose_name='ID', auto_created=True)),
                ('request_name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reserved',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True,
                                        verbose_name='ID', auto_created=True)),
                ('reserved', models.DateField(auto_now=True)),
                ('equipment', models.ForeignKey(to='system.Equipment')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True,
                                        verbose_name='ID', auto_created=True)),
                ('meta_data', models.CharField(max_length=50)),
                ('equipment_name', models.ForeignKey(to='system.Equipment')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True,
                                        verbose_name='ID', auto_created=True)),
                ('tag', models.CharField(max_length=255)),
                ('equipment', models.ForeignKey(to='system.Equipment')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True,
                                        verbose_name='ID', auto_created=True)),
                ('request', models.ForeignKey(to='system.Request')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
