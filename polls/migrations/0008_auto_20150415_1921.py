# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_events'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='events',
        ),
        migrations.RemoveField(
            model_name='category',
            name='rank',
        ),
        migrations.AddField(
            model_name='eve',
            name='category',
            field=models.ForeignKey(default=0, to='polls.Category'),
            preserve_default=False,
        ),
    ]
