# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20150813_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='CT_property',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'\xe6\xba\xb6\xe9\xaa\xa8'), (2, b'\xe6\x88\x90\xe9\xaa\xa8'), (3, b'\xe6\xb7\xb7\xe5\x90\x88')]),
        ),
        migrations.AddField(
            model_name='test',
            name='X_ray',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'\xe6\xad\xa3\xe5\xb8\xb8'), (2, b'\xe5\x8d\x8a\xe8\x84\xb1\xe4\xbd\x8d/\xe6\xbb\x91\xe7\xa7\xbb'), (3, b'\xe4\xbe\xa7\xe5\x87\xb8/\xe5\x90\x8e\xe5\x87\xb8')]),
        ),
        migrations.AddField(
            model_name='test',
            name='collapse',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'<50%'), (2, b'>50%'), (3, b'\xe5\x8f\x97\xe7\xb4\xaf>50%\xe4\xbd\x86\xe6\x97\xa0\xe5\xa1\x8c\xe9\x99\xb7'), (4, b'\xe6\x97\xa0')]),
        ),
        migrations.AddField(
            model_name='test',
            name='diagosis',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='test',
            name='enneking',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='test',
            name='lateral_involvement',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'\xe6\x98\xaf'), (2, b'\xe5\x90\xa6'), (3, b'\xe4\xb8\x8d\xe6\xb6\x89\xe5\x8f\x8a')]),
        ),
        migrations.AddField(
            model_name='test',
            name='pre_test',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'\xe6\x98\xaf'), (2, b'\xe5\x90\xa6')]),
        ),
        migrations.AddField(
            model_name='test',
            name='project_date',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='test',
            name='project_name',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'\xe6\x89\x8b\xe6\x9c\xaf\xe7\x97\x85\xe7\x90\x86'), (2, b'\xe7\xa9\xbf\xe5\x88\xba\xe7\x97\x85\xe7\x90\x86'), (3, b'PET-CT'), (4, b'\xe7\x97\x85\xe5\x8f\x98MR'), (5, b'\xe7\x97\x85\xe5\x8f\x98CT'), (6, b'\xe7\x97\x85\xe5\x8f\x98X\xe7\xba\xbf\xe7\x89\x87'), (7, b'\xe9\xaa\xa8\xe6\x89\xab\xe6\x8f\x8f')]),
        ),
        migrations.AddField(
            model_name='test',
            name='result_discription',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='test',
            name='vertebral_artery_involvement',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='test',
            name='wbb_1_12',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='test',
            name='wbb_A_F',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
