# Generated by Django 2.2.6 on 2020-09-30 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_transaction_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartcbid',
            name='ticket',
        ),
        migrations.RemoveField(
            model_name='cartproduct',
            name='product_type',
        ),
        migrations.DeleteModel(
            name='Reconcile',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carts.Cart'),
        ),
        migrations.DeleteModel(
            name='CartCBID',
        ),
        migrations.DeleteModel(
            name='CartProduct',
        ),
    ]
