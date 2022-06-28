# Generated by Django 4.0.5 on 2022-06-28 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistrationData',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('email_code', models.CharField(max_length=64, verbose_name='код верифікації пошти')),
                ('email_confirmed', models.BooleanField(default=False, verbose_name='чи підтвердив користувач реєстрацію')),
            ],
            options={
                'abstract': False,
            },
            bases=('users.user',),
        ),
    ]
