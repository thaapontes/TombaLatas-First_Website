# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perfis', '0002_convite'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilcao',
            name='usuario',
            field=models.OneToOneField(related_name='perfil', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
