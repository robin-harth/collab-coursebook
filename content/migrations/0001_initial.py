# Generated by Django 3.2.5 on 2022-01-24 16:47

import content.mixin
import content.validator
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageContent',
            fields=[
                ('content', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='base.content', verbose_name='Content')),
                ('source', models.TextField(verbose_name='Source')),
                ('license', models.CharField(blank=True, max_length=200, verbose_name='License')),
                ('image', models.ImageField(upload_to='uploads/contents/%Y/%m/%d/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Image Content',
                'verbose_name_plural': 'Image Contents',
            },
            bases=(models.Model, content.mixin.GeneratePreviewMixin),
        ),
        migrations.CreateModel(
            name='Latex',
            fields=[
                ('content', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='base.content', verbose_name='Content')),
                ('pdf', models.FileField(blank=True, upload_to='uploads/contents/%Y/%m/%d/', validators=[content.validator.Validator.validate_pdf], verbose_name='PDF')),
                ('textfield', models.TextField(help_text='Please insert only valid LaTeX code. The packages and \\begin{document} and \\end{document} will be inserted automatically.', verbose_name='Latex Code')),
                ('source', models.TextField(verbose_name='Source')),
            ],
            options={
                'verbose_name': 'Latex Content',
                'verbose_name_plural': 'Latex Contents',
            },
            bases=(models.Model, content.mixin.GeneratePreviewMixin),
        ),
        migrations.CreateModel(
            name='MDContent',
            fields=[
                ('content', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='base.content', verbose_name='Content')),
                ('md', models.FileField(blank=True, upload_to='uploads/contents/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(['md'])], verbose_name='Markdown File')),
                ('textfield', models.TextField(blank=True, help_text='Insert your Markdown script here:', verbose_name='Markdown Script')),
                ('source', models.TextField(verbose_name='Source')),
            ],
            options={
                'verbose_name': 'MD Content',
                'verbose_name_plural': 'MD Contents',
            },
            bases=(models.Model, content.mixin.GeneratePreviewMixin),
        ),
        migrations.CreateModel(
            name='PDFContent',
            fields=[
                ('content', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='base.content', verbose_name='Content')),
                ('pdf', models.FileField(blank=True, upload_to='uploads/contents/%Y/%m/%d/', validators=[content.validator.Validator.validate_pdf], verbose_name='PDF')),
                ('source', models.TextField(verbose_name='Source')),
                ('license', models.CharField(blank=True, max_length=200, verbose_name='License')),
            ],
            options={
                'verbose_name': 'PDF Content',
                'verbose_name_plural': 'PDF Contents',
            },
            bases=(models.Model, content.mixin.GeneratePreviewMixin),
        ),
        migrations.CreateModel(
            name='TextField',
            fields=[
                ('content', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='base.content', verbose_name='Content')),
                ('textfield', models.TextField(verbose_name='Text')),
                ('source', models.TextField(verbose_name='Source')),
            ],
            options={
                'verbose_name': 'Textfield Content',
                'verbose_name_plural': 'Textfield Contents',
            },
            bases=(models.Model, content.mixin.GeneratePreviewMixin),
        ),
        migrations.CreateModel(
            name='YTVideoContent',
            fields=[
                ('content', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='base.content', verbose_name='Content')),
                ('url', models.URLField(validators=[content.validator.Validator.validate_youtube_url], verbose_name='Video URL')),
            ],
            options={
                'verbose_name': 'YouTube Video Content',
                'verbose_name_plural': 'YouTube Video Contents',
            },
            bases=(models.Model, content.mixin.GeneratePreviewMixin),
        ),
    ]
