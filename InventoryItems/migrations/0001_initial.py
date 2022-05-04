# Generated by Django 4.0.4 on 2022-05-04 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default=None, max_length=200, null=True)),
                ('extra_from_checklist_amount', models.IntegerField(default=0)),
                ('completed_status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('edited_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]