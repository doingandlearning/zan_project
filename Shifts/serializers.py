from pdb import post_mortem
from rest_framework import serializers
from .models import Shift, CheckListItem
from Checklists.models import Checklist


class ShiftSerializer(serializers.ModelSerializer):
    # checklist
    # worker_worked
    # worker_worker confirmed
    # department
    class Meta:
        model = Shift
        fields = '__all__'

    def create(self, data):
        # checklist ids -> which checklists are needed for this shift ...
        checklist_ids = data.pop("checklist_ids")
        new_shift = Shift(data)

        new_shift.save()

        for id in checklist_ids:
            # get the checklist
            current_checklist = Checklist.objects.get(pk=id)
            # iterate over the tasks and create checklist_items
            for task in current_checklist.tasks:
                item = CheckListItem(name=task.name, category="Task")
                item.save()
                new_shift.checklist.add(item)
            # iterate over the items and create checklist_items
            for item in current_checklist.items:
                cl_item = CheckListItem(name=item.name, category="Item")
                cl_item.save()
                new_shift.checklist.add(cl_item)

        return new_shift
