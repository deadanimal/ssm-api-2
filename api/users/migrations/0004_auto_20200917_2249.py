# Generated by Django 2.2.6 on 2020-09-17 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200917_2018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='package',
            new_name='egov_package',
        ),
    ]
