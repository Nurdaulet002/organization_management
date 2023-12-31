# Generated by Django 3.2.5 on 2021-12-09 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipment_system', '0001_initial'),
        ('account', '0001_initial'),
        ('technological_card', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('document_circulation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('price', models.DecimalField(decimal_places=0, max_digits=19)),
                ('duration', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_system.categoryservice')),
                ('equipments', models.ManyToManyField(blank=True, to='equipment_system.Equipment')),
                ('technological_cards', models.ManyToManyField(blank=True, to='technological_card.TechnologicalCard')),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=0, max_digits=19, null=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_services', to='service_system.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FormService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.company')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document_circulation.form')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_system.service')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
