# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eve',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=2000)),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='events',
            field=models.ForeignKey(to='polls.Eve'),
        ),
    ]
