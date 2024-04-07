# Generated by Django 5.0.2 on 2024-02-28 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.TextField()),
                ('product_price', models.TextField()),
                ('product_stock', models.TextField()),
            ],
            options={
                'db_table': 'tbl_product',
            },
        ),
    ]