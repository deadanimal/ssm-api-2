# Generated by Django 2.2.6 on 2020-09-17 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200917_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('AD', 'Admin'), ('CB', 'CBID'), ('EG', 'eGovernment'), ('PB', 'Public')], default='PB', max_length=2),
        ),
    ]
