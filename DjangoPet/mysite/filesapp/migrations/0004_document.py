# Generated by Django 4.1.6 on 2023-02-18 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filesapp', '0003_alter_fileuploaded_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='documents')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]