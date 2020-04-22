# Generated by Django 3.0.4 on 2020-04-22 13:50

from django.db import migrations
import user.managers


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', user.managers.CustomUserManager()),
            ],
        ),
    ]
