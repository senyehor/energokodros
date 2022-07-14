# Generated by Django 4.0.5 on 2022-07-14 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_userrole_is_active_user_is_active'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='userrole',
            constraint=models.UniqueConstraint(fields=('user', 'institution', 'access_level'), name='user_has_unique_access_level_for_institution'),
        ),
    ]
