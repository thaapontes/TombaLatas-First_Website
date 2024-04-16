# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0003_perfilcao_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilcao',
            name='tipo',
            field=models.CharField(default=b'SOME STRING', max_length=255),
            preserve_default=True,
        ),
    ]
