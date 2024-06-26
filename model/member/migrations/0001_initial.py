# Generated by Django 5.0.2 on 2024-02-26 09:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('member_email', models.CharField(max_length=50)),
                ('member_password', models.CharField(max_length=20)),
                ('member_name', models.TextField()),
                ('member_age', models.IntegerField(default=0)),
                ('member_status', models.BooleanField(default=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tbl_member',
            },
        ),
    ]
