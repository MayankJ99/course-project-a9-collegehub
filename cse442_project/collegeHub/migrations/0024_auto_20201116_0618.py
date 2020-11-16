# Generated by Django 3.1.2 on 2020-11-16 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeHub', '0023_auto_20201106_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='day',
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(help_text='Final time', verbose_name='Final time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(help_text='Starting time', verbose_name='Starting time'),
        ),
    ]
