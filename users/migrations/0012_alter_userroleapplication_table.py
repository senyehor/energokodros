# Generated by Django 4.0.5 on 2022-07-14 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_userrole_user_has_unique_access_level_for_institution'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userroleapplication',
            table='users_roles_applications',
        ),
    ]
