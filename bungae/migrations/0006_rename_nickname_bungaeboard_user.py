# Generated by Django 3.2.5 on 2022-01-25 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bungae', '0005_rename_user_id_bungaeboard_nickname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bungaeboard',
            old_name='nickname',
            new_name='User',
        ),
    ]
