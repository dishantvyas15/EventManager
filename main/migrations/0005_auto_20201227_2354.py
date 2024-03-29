# Generated by Django 3.1.4 on 2020-12-27 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_event_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participantName', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('proofLink', models.CharField(blank=True, max_length=10000)),
                ('regType', models.CharField(max_length=10)),
                ('noOfTickets', models.IntegerField()),
                ('eventID', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='event',
            old_name='regEmail',
            new_name='hostEmail',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='regPswd',
            new_name='hostPswd',
        ),
    ]
