# Generated by Django 3.0.4 on 2020-03-25 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('idNumber', models.CharField(max_length=100)),
                ('uniqueID', models.CharField(max_length=100)),
                ('mobileNo', models.CharField(max_length=100)),
                ('pin', models.IntegerField()),
            ],
            options={
                'db_table': 'tbl_customers',
            },
        ),
    ]
