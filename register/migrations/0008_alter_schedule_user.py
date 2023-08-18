# Generated by Django 3.2.5 on 2022-01-13 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('register', '0007_alter_schedule_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
