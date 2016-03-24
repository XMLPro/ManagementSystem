# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('equipment', models.ForeignKey(to='system.Equipment')),
            ],
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='tag',
            new_name='tag_name',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='equipment',
        ),
        migrations.AddField(
            model_name='tagmanagement',
            name='tag',
            field=models.ForeignKey(to='system.Tag'),
        ),
    ]
