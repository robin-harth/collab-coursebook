# Generated by Django 3.0.7 on 2021-02-07 10:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20210130_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textfield',
            name='textfield',
            field=ckeditor.fields.RichTextField(verbose_name='Text'),
        ),
    ]
