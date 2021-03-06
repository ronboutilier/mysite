# Generated by Django 3.1.6 on 2021-02-14 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('steamroller', '0011_auto_20210214_1738'),
	('ronboutilier', '0004_auto_20210214_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessory_lift_1',
            name='accessory_1_lift_date',
        ),
        migrations.RemoveField(
            model_name='accessory_lift_2',
            name='accessory_2_lift_date',
        ),
        migrations.RemoveField(
            model_name='assistance_lift_1',
            name='assistance_1_lift_date',
        ),
        migrations.RemoveField(
            model_name='assistance_lift_2',
            name='assistance_2_lift_date',
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
        migrations.RemoveField(
            model_name='health',
            name='health_date',
        ),
        migrations.RemoveField(
            model_name='primary_lift',
            name='primary_lift_date',
        ),
        migrations.RemoveField(
            model_name='supplements',
            name='supplements_date',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='Lifter',
        ),
        migrations.DeleteModel(
            name='Accessory_Lift_1',
        ),
        migrations.DeleteModel(
            name='Accessory_Lift_2',
        ),
        migrations.DeleteModel(
            name='Assistance_Lift_1',
        ),
        migrations.DeleteModel(
            name='Assistance_Lift_2',
        ),
        migrations.DeleteModel(
            name='Health',
        ),
        migrations.DeleteModel(
            name='Primary_Lift',
        ),
        migrations.DeleteModel(
            name='Supplements',
        ),
        migrations.DeleteModel(
            name='Workout',
        ),
    ]
