# Generated by Django 2.0.5 on 2018-05-07 10:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sleepsetting',
            name='friday',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sleepsetting',
            name='from_hour',
            field=models.TimeField(default=datetime.datetime(2018, 5, 7, 10, 30, 30, 50176)),
        ),
        migrations.AlterField(
            model_name='sleepsetting',
            name='monday',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sleepsetting',
            name='saturday',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sleepsetting',
            name='sunday',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sleepsetting',
            name='thursday',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sleepsetting',
            name='to_hour',
            field=models.TimeField(default=datetime.datetime(2018, 5, 7, 10, 40, 30, 50176)),
        ),
        migrations.AlterField(
            model_name='sleepsetting',
            name='tuesday',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sleepsetting',
            name='wednesday',
            field=models.BooleanField(default=False),
        ),
    ]