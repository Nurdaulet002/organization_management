# Generated by Django 3.2.5 on 2021-12-20 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Администратор'), (2, 'Координатор'), (3, 'Доктор')]),
        ),
    ]
