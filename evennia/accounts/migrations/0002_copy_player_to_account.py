# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 19:17
from __future__ import unicode_literals

from django.apps import apps as global_apps
from django.db import migrations


def forwards(apps, schema_editor):
    try:
        PlayerDB = apps.get_model('players', 'PlayerDB')
    except LookupError:
        # playerdb not available. Skip.
        return

    AccountDB = apps.get_model('accounts', 'AccountDB')
    for player in PlayerDB.objects.all():
        account = AccountDB(id=player.id,
                            password=player.password,
                            is_superuser=player.is_superuser,
                            last_login=player.last_login,
                            username=player.username,
                            first_name=player.first_name,
                            last_name=player.last_name,
                            email=player.email,
                            is_staff=player.is_staff,
                            is_active=player.is_active,
                            date_joined=player.date_joined,
                            db_key=player.db_key,
                            db_typeclass_path=player.db_typeclass_path,
                            db_date_created=player.db_date_created,
                            db_lock_storage=player.db_lock_storage,
                            db_is_connected=player.db_is_connected,
                            db_cmdset_storage=player.db_cmdset_storage,
                            db_is_bot=player.db_is_bot)
        account.save()
        for group in player.groups.all():
            account.groups.add(group)
        for user_permission in player.user_permissions.all():
            account.user_permissions.add(user_permission)
        for attr in player.db_attributes.all():
            account.db_attributes.add(attr)
        for tag in player.db_tags.all():
            account.db_tags.add(tag)


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop)
    ]

    if global_apps.is_installed('players'):
        dependencies.append(('players', '0006_auto_20170606_1731'))