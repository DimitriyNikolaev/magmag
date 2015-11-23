# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_auto_20140922_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_added',
            field=models.DateField(verbose_name='Date_Added', editable=False, default=datetime.datetime(2014, 12, 18, 21, 4, 53, 47939)),
            preserve_default=True,
        ),
    ]
