# Generated by Django 4.0.4 on 2022-05-05 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Checklists', '0005_delete_inventoryitem_delete_subsection_delete_task_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checklist',
            old_name='cheklist_sections',
            new_name='checklist_sections',
        ),
    ]
