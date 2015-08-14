# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20150813_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='DB_ID',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='EMR_id',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='patient',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
