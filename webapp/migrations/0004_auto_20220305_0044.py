# Generated by Django 3.1.4 on 2022-03-04 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_userexcuse_excuse_id'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userexcuse',
            table='user_excuses',
        ),
    ]
