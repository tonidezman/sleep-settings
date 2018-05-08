from django.utils import timezone
from django.db import models

class SleepSetting(models.Model):
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)

    from_time = models.TimeField(default="00:00")
    to_time = models.TimeField(default="06:00")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'id: {self.id} from_time: {self.from_time} to_time: {self.to_time}'
