# Generated by Django 2.0.3 on 2018-09-23 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0003_remove_block_st'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
