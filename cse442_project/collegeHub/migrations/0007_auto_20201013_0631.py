# Generated by Django 3.0.4 on 2020-10-13 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collegeHub', '0006_auto_20201011_1002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experiences',
            old_name='userProfile',
            new_name='profile',
        ),
    ]
