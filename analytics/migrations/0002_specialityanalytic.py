# Generated by Django 3.2.5 on 2022-01-13 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_speciality_company'),
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialityAnalytic',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('account.speciality',),
        ),
    ]
