# Generated by Django 2.1.2 on 2018-11-04 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carton', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='prereqs',
        ),
    ]