# Generated by Django 2.2.6 on 2020-09-23 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_ticket_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketcbid',
            name='status',
            field=models.CharField(choices=[('PG', 'Pending'), ('PD', 'Paid'), ('CP', 'Completed')], default='PG', max_length=2),
        ),
    ]
