# Generated by Django 3.0.4 on 2020-03-26 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_currency_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='accountBalance',
            field=models.FloatField(),
        ),
    ]