# Generated by Django 3.2.5 on 2022-02-02 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_circulation', '0005_auto_20220202_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='old_id',
            field=models.IntegerField(),
        ),
    ]
