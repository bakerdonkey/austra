# Generated by Django 2.1.3 on 2018-11-25 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carton', '0003_auto_20181124_0441'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instructor',
            options={'permissions': (('can_create_instructor', ''),)},
        ),
    ]