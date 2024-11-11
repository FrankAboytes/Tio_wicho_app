# Generated by Django 5.1.1 on 2024-11-11 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_bebida'),
    ]

    operations = [
        migrations.AddField(
            model_name='bebida',
            name='categoria',
            field=models.CharField(default='Bebida', max_length=100),
        ),
        migrations.AlterField(
            model_name='bebida',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]