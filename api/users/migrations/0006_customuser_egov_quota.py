# Generated by Django 2.2.6 on 2020-09-22 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200917_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='egov_quota',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
