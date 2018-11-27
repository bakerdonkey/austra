# Generated by Django 2.1.2 on 2018-11-27 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carton', '0011_auto_20181126_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='courses_dooted',
        ),
        migrations.AddField(
            model_name='profile',
            name='courses_downdooted',
            field=models.ManyToManyField(related_name='downdooted', to='carton.Course'),
        ),
        migrations.AddField(
            model_name='profile',
            name='courses_updooted',
            field=models.ManyToManyField(related_name='updooted', to='carton.Course'),
        ),
    ]
