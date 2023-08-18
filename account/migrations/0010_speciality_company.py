# Generated by Django 3.2.5 on 2022-01-13 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_user_speciality'),
    ]

    operations = [
        migrations.AddField(
            model_name='speciality',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.company'),
            preserve_default=False,
        ),
    ]