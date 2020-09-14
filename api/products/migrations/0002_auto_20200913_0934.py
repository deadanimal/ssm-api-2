# Generated by Django 2.2.6 on 2020-09-13 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='NA'),
        ),
        migrations.AddField(
            model_name='product',
            name='fee',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='is_bilingual',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='is_ctc',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='is_document',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='middleware_service',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='NA', max_length=100),
        ),
    ]
