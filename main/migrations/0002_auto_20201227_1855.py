# Generated by Django 3.1.4 on 2020-12-27 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='Desc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='Loc',
            new_name='loc',
        ),
    ]