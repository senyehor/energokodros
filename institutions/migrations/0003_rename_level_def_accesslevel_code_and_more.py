# Generated by Django 4.0.5 on 2022-07-14 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0002_alter_accesslevel_options_alter_institution_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accesslevel',
            old_name='level_def',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='accesslevel',
            old_name='level_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='institution',
            old_name='institution_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='object',
            old_name='object_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='object',
            old_name='object_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='institution',
            name='institution_description',
        ),
        migrations.AddField(
            model_name='institution',
            name='description',
            field=models.TextField(db_column='institution_description', default='', verbose_name='опис закладу'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accesslevel',
            name='code',
            field=models.IntegerField(db_column='level_def', unique=True, verbose_name='код рівню доступу'),
        ),
        migrations.AlterField(
            model_name='accesslevel',
            name='description',
            field=models.TextField(db_column='level_description', verbose_name='опис рівню доступу'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='institution_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='institution',
            name='name',
            field=models.CharField(db_column='institution_name', max_length=1000, verbose_name='назва закладу'),
        ),
        migrations.AlterField(
            model_name='object',
            name='description',
            field=models.TextField(blank=True, db_column='object_description', null=True, verbose_name="опис об'єкту"),
        ),
        migrations.AlterField(
            model_name='object',
            name='name',
            field=models.CharField(blank=True, db_column='object_name', max_length=1000, verbose_name="назва об'єкту"),
        ),
    ]