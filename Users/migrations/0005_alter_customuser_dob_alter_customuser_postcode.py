# Generated by Django 4.0.4 on 2022-05-05 23:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_customuser_postcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='DOB',
            field=models.DateField(default=datetime.date(2022, 5, 6)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='postcode',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]
