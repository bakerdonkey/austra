# Generated by Django 2.1.1 on 2018-11-05 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carton', '0005_merge_20181105_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='prereqs',
            field=models.ManyToManyField(blank=True, related_name='_course_prereqs_+', to='carton.Course'),
        ),
    ]