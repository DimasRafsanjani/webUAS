# Generated by Django 4.1.5 on 2023-01-21 04:30

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('CrudMahasiswa', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='tbl_mahasiswadetails',
            managers=[
                ('ddlmahasiswaobjects', django.db.models.manager.Manager()),
            ],
        ),
    ]
