# Generated by Django 2.1.2 on 2018-11-26 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carton', '0009_auto_20181126_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='credits',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='profile',
            name='user_email',
            field=models.CharField(default='example@gmail.com', help_text='Enter your email', max_length=100),
        ),
    ]
