# Generated by Django 3.2.5 on 2022-01-24 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50, unique=True)),
                ('user_pw', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'user',
                'managed': True,
            },
        ),
    ]
