# Generated by Django 3.2.6 on 2021-08-02 20:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateUserForms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('login_count', models.IntegerField()),
                ('Last_login_time', models.DateTimeField()),
                ('Timestamps', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
