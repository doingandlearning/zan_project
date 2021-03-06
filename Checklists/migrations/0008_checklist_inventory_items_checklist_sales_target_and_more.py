# Generated by Django 4.0.4 on 2022-05-05 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryItems', '0002_inventoryitem_order'),
        ('Tasks', '0004_task_completed_by_task_completed_status_task_order'),
        ('Checklists', '0007_remove_checklist_checklist_sections'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist',
            name='inventory_items',
            field=models.ManyToManyField(blank=True, related_name='checklist_items', to='InventoryItems.inventoryitem'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='sales_target',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='checklist',
            name='tasks',
            field=models.ManyToManyField(blank=True, related_name='checklist_tasks', to='Tasks.task'),
        ),
    ]
