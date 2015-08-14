# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20150813_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptom',
            name='duration',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
