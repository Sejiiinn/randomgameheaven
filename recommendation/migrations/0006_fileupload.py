# Generated by Django 4.0.1 on 2022-01-27 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0005_merge_20220127_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgfile', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
