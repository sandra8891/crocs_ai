# Generated by Django 5.2 on 2025-05-14 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0006_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(blank=True, max_length=36, null=True, verbose_name='Payment ID'),
        ),
        migrations.AddField(
            model_name='order',
            name='provider_order_id',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Order ID'),
        ),
        migrations.AddField(
            model_name='order',
            name='signature_id',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Signature ID'),
        ),
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
