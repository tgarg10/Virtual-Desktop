# Generated by Django 3.2.11 on 2022-02-06 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bit95', '0018_auto_20220206_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deleted_files',
            name='date_deleted',
            field=models.CharField(default='06/02/22', max_length=64),
        ),
    ]
