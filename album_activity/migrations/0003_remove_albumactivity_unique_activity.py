# Generated by Django 3.2.8 on 2021-10-13 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album_activity', '0002_auto_20211013_2029'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='albumactivity',
            name='unique_activity',
        ),
    ]
