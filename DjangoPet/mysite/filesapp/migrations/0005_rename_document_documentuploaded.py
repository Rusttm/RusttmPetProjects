# Generated by Django 4.1.6 on 2023-02-19 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filesapp', '0004_document'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Document',
            new_name='DocumentUploaded',
        ),
    ]