# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_auto_20160214_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='equipment',
            name='borrower',
            field=models.ForeignKey(to='default.UserSocialAuth'),
        ),
        migrations.AlterField(
            model_name='log',
            name='user',
            field=models.ForeignKey(to='default.UserSocialAuth'),
        ),
        migrations.AlterField(
            model_name='reserved',
            name='user',
            field=models.ForeignKey(to='default.UserSocialAuth'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(to='default.UserSocialAuth'),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
