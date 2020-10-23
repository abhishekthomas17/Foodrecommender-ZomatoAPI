# Generated by Django 3.0.2 on 2020-10-05 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('minutes', models.IntegerField(blank=True, null=True)),
                ('desciription', models.CharField(blank=True, max_length=50000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desciription', models.CharField(blank=True, max_length=10000, null=True)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_module.dish')),
            ],
        ),
        migrations.CreateModel(
            name='ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_module.dish')),
            ],
        ),
    ]
