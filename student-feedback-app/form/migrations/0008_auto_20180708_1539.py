# Generated by Django 2.0.5 on 2018-07-08 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_auto_20180708_1538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professor',
            old_name='roll_no',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='roll_no',
            new_name='username',
        ),
    ]
