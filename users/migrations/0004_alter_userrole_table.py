# Generated by Django 4.0.4 on 2022-06-21 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userregistrationrequest'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userrole',
            table='users_roles',
        ),
    ]
