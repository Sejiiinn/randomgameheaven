# Generated by Django 3.2.5 on 2022-01-25 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bungae', '0004_alter_bungaeboard_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bungaeboard',
            old_name='user_id',
            new_name='nickname',
        ),
    ]