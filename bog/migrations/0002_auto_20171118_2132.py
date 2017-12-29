# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(help_text=b'\xe6\xa0\x87\xe9\xa2\x98', max_length=20),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(help_text=b'\xe8\xaf\x84\xe8\xae\xba', max_length=200),
        ),
    ]
