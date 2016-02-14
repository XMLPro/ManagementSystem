# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='borrowed_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='borrowed_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='reserved',
            name='reserved',
            field=models.DateField(auto_now=True),
        ),
    ]
