from datetime import date
from django.db import models

# Create your models here.


class Shift(models.Model):
    name = models.CharField(max_length=50, default=None)
    description = models.CharField(max_length=250, default=None)
    date = models.DateField(blank=True, null=True, )
    start_time = models.TimeField()
    end_time = models.TimeField()
    # departmentID
    # createdBy

    # feedback
    # rating
    # confirmedBy
    # workerID
    def __str__(self):
        return f"{self.name} - {self.description}"
