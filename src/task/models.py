from django.db import models

from account.models import User
from TaskManager import myForm


class Task(models.Model):
    title       = models.CharField(max_length=124)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    task_type        = myForm.TaskTypeField()
    repeat      = myForm.DayOfTheWeekField()

    def __str__(self):
        return self.title