# Generated by Django 4.0.4 on 2022-05-04 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subsection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('edited_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]