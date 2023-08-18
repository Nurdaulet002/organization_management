# Generated by Django 3.2.5 on 2022-01-12 23:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('register', '0004_auto_20220112_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='register',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_register', to=settings.AUTH_USER_MODEL),
        ),
    ]
