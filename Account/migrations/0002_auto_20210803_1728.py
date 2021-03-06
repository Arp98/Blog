# Generated by Django 3.2.6 on 2021-08-03 11:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('login_count', models.IntegerField()),
                ('Last_login_time', models.DateTimeField(auto_now_add=True, verbose_name='Last Login')),
                ('Timestamps', models.DateTimeField(default=datetime.datetime.now, verbose_name='Timestamps')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='CreateUserForms',
        ),
    ]
