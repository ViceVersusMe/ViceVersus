# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
        ('vice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gift_cards',
            field=models.ForeignKey(to='vice.GiftCard'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_name',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
