# Generated by Django 4.1.5 on 2023-01-22 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrudDeveloper', '0008_developer_delete_mahasiswa'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='developerExpYear',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]