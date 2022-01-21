# Generated by Django 3.2.3 on 2022-01-21 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='quantity of items'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='deal_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deals.deals'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='price',
            field=models.FloatField(verbose_name='price of the item'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='quantity of items'),
        ),
    ]
