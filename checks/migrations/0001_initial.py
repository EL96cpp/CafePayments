# Generated by Django 5.0.6 on 2024-06-18 08:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0002_customercard_discount'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.SmallIntegerField()),
                ('total_no_discount', models.IntegerField()),
                ('total_with_discount', models.IntegerField()),
                ('order', models.JSONField()),
                ('date', models.DateTimeField()),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='customers.customercard')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employees.employee')),
            ],
        ),
    ]