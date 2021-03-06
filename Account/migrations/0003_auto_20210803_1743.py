# Generated by Django 3.2.6 on 2021-08-03 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_auto_20210803_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='login_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]
