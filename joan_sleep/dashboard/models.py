from django.utils import timezone
from datetime import timedelta
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

    @classmethod
    def should_sleep(cls):
        setting = cls.objects.first()
        now = timezone.now()
        day_text = now.strftime("%A").lower()

        # here we check if settings date and current date match
        if getattr(setting, day_text):
            if setting.from_time <= now.time() <= setting.to_time:
                return False
            elif now.time() < setting.from_time:
                return setting._format_datetime(now)
        date = setting._find_next_awake_day(now)
        return setting._format_datetime(date)

    def _find_next_awake_day(self, date):
        weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        current_weekday = date.weekday()
        for offset in range(1, 8):
            indx = (offset + current_weekday) % 7
            if getattr(self, weekdays[indx]):
                return date + timedelta(offset)
        raise Exception("Settings should have at least one weekday chosen.")

    def _format_datetime(self, date):
        date = date.strftime("%Y-%m-%dT")
        from_time = self.from_time.strftime("%R")
        to_time = self.to_time.strftime("%R")
        return f'{date}{from_time}-{to_time}'
