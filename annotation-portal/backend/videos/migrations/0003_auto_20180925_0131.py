# Generated by Django 2.0.3 on 2018-09-25 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_video_num_annotations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='VideoID',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
