# Generated by Django 2.0.5 on 2018-07-08 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0008_auto_20180708_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professor',
            old_name='username',
            new_name='roll_no',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='username',
            new_name='roll_no',
        ),
    ]