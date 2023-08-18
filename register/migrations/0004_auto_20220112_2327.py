# Generated by Django 3.2.5 on 2022-01-12 23:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('register', '0003_worktime_register'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worktime',
            name='register',
        ),
        migrations.AddField(
            model_name='schedule',
            name='register',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='register', to='account.user'),
            preserve_default=False,
        ),
    ]