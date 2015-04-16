# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_delete_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first', models.CharField(default=b'?', max_length=2000)),
                ('second', models.CharField(default=b'?', max_length=2000)),
                ('third', models.CharField(default=b'?', max_length=2000)),
            ],
        ),
    ]
