# Generated by Django 3.2.11 on 2022-02-02 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bit95', '0014_auto_20220202_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deleted_files',
            name='date_deleted',
            field=models.CharField(default='02-02-2022', max_length=64),
        ),
        migrations.AlterField(
            model_name='files',
            name='date_time_created',
            field=models.CharField(default='02-02-2022', max_length=64),
        ),
    ]
