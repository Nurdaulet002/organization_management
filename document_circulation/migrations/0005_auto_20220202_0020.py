# Generated by Django 3.2.5 on 2022-02-02 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_circulation', '0004_alter_marker_kind'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='old_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='marker',
            name='kind',
            field=models.CharField(choices=[('text', 'Ввод текста'), ('textarea', 'textarea'), ('select', 'select'), ('parent', 'parent'), ('datalist', 'datalist'), ('mkb10', 'mkb10'), ('pacient', 'pacient'), ('label', 'label'), ('datepicker', 'datepicker'), ('currentDate', 'currentDate'), ('checkbox', 'checkbox'), ('doctor', 'doctor'), ('currentTime', 'currentTime'), ('hidden', 'hidden'), ('mkb9', 'mkb9'), ('radio', 'radio'), ('nowdate', 'nowdate'), ('time', 'time'), ('drugs', 'drugs'), ('profile_bunk', 'profile_bunk'), ('scheme_chemotherapy', 'scheme_chemotherapy'), ('morphological_type', 'morphological_type'), ('postoperative_complication', 'postoperative_complication'), ('head', 'head'), ('departments', 'departments'), ('doctors', 'doctors'), ('doctors_bg', 'doctors_bg'), ('service', 'service'), ('multiple_parent', 'multiple_parent'), ('multiple_form_parent', 'multiple_form_parent')], default='text', max_length=80),
        ),
    ]
