# Generated by Django 3.2.5 on 2022-01-13 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_alter_schedule_register'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worktimeexclusion',
            name='content_type',
        ),
        migrations.DeleteModel(
            name='WorkTime',
        ),
        migrations.DeleteModel(
            name='WorkTimeExclusion',
        ),
    ]
