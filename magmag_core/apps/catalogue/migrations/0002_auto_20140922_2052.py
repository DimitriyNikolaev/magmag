# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2014, 9, 22, 20, 52, 46, 312606), verbose_name='Date_Added', editable=False),
        ),
    ]
