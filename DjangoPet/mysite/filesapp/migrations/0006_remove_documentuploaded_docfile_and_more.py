# Generated by Django 4.1.6 on 2023-02-19 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filesapp', '0005_rename_document_documentuploaded'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentuploaded',
            name='docfile',
        ),
        migrations.AddField(
            model_name='documentuploaded',
            name='upload',
            field=models.FileField(default=0, upload_to='documents/'),
            preserve_default=False,
        ),
    ]
