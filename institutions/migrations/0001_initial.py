# Generated by Django 4.0.5 on 2022-06-26 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessLevel',
            fields=[
                ('access_level_id', models.AutoField(primary_key=True, serialize=False)),
                ('level_def', models.IntegerField(unique=True, verbose_name='код рівню доступу')),
                ('level_description', models.TextField(verbose_name='опис рівню доступу')),
            ],
            options={
                'db_table': 'access_levels',
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('institution_id', models.AutoField(db_column='institution_id', primary_key=True, serialize=False)),
                ('institution_name', models.CharField(max_length=1000, verbose_name='назва закладу')),
                ('institution_description', models.TextField(verbose_name='опис закiладу')),
            ],
            options={
                'db_table': 'institutions',
            },
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('object_id', models.AutoField(primary_key=True, serialize=False)),
                ('object_name', models.CharField(blank=True, max_length=1000, verbose_name="назва об'єкту")),
                ('object_description', models.TextField(blank=True, null=True, verbose_name="опис об'єкту")),
                ('access_level', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='institutions.accesslevel')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_objects', to='institutions.institution')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='institutions.object')),
            ],
            options={
                'db_table': 'objects',
            },
        ),
    ]
