# Generated by Django 3.2.5 on 2022-02-19 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_circulation', '0010_alter_marker_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formhistory',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='formhistory',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
