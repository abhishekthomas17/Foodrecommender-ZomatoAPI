# Generated by Django 3.0.2 on 2020-10-05 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_module', '0003_auto_20201005_2232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='desciription',
            new_name='description',
        ),
    ]
