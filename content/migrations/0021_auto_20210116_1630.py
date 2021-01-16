# Generated by Django 3.0.7 on 2021-01-16 15:30

import content.validator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0020_auto_20210112_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latex',
            name='pdf',
            field=models.FileField(blank=True, upload_to='uploads/contents/%Y/%m/%d/', validators=[content.validator.validate_is_pdf], verbose_name='PDF'),
        ),
        migrations.AlterField(
            model_name='pdfcontent',
            name='pdf',
            field=models.FileField(blank=True, upload_to='uploads/contents/%Y/%m/%d/', validators=[content.validator.validate_is_pdf], verbose_name='PDF'),
        ),
    ]
