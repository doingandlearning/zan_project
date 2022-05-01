# Generated by Django 4.0.4 on 2022-05-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50, unique=True)),
                ('description', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('image', models.CharField(blank=True, default=None, max_length=200, null=True)),
            ],
        ),
    ]
