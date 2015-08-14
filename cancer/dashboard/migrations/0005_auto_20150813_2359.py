# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20150813_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='followup',
            name='DB_ID',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='followup',
            name='EMR_id',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='followup',
            name='name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='DB_ID',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='EMR_id',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='test',
            name='DB_ID',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='test',
            name='EMR_id',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='test',
            name='name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='followup',
            name='patient',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='patient',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='patient',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
