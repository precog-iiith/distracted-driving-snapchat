# Generated by Django 2.0.3 on 2018-09-23 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='num_annotations',
            field=models.IntegerField(default=0),
        ),
    ]
