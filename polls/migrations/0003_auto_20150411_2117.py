# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cId',
            new_name='CId',
        ),
        migrations.AddField(
            model_name='category',
            name='events',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]
