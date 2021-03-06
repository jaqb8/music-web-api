# Generated by Django 3.2.8 on 2021-10-13 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album_activity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumactivity',
            name='activity',
            field=models.CharField(blank=True, choices=[('WTL', 'want to listen')], max_length=3),
        ),
        migrations.AddConstraint(
            model_name='albumactivity',
            constraint=models.UniqueConstraint(fields=('user', 'album_id'), name='unique_activity'),
        ),
    ]
