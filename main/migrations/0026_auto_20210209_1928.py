# Generated by Django 3.1.6 on 2021-02-09 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20210209_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bridge',
            name='element_history',
            field=models.FileField(null=True, upload_to='history/'),
        ),
    ]
