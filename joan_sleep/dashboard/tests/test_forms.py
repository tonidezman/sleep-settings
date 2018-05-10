from django.test import TestCase
from datetime import time

from dashboard.models import SleepSetting
from dashboard.forms import SleepSettingsForm

class SleepSettingsFormTest(TestCase):
    def setUp(self):
        setting = SleepSetting()
        setting.monday = True
        setting.save()

    def test_valid_form_with_correct_from_and_to_time(self):
        self.assertEqual(SleepSetting.objects.count(), 1)
        setting = SleepSetting.objects.first()
        setting.from_time = time(6, 0)
        setting.to_time = time(7, 0)
        data = {
            "monday": setting.monday,
            "tuesday": setting.tuesday,
            "wednesday": setting.wednesday,
            "thursday": setting.thursday,
            "friday": setting.friday,
            "saturday": setting.saturday,
            "sunday": setting.sunday,
            "from_time": setting.from_time,
            "to_time": setting.to_time,
        }
        form = SleepSettingsForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_with_for_from_and_to_time(self):
        self.assertEqual(SleepSetting.objects.count(), 1)
        setting = SleepSetting.objects.first()
        setting.from_time = time(6, 0)
        setting.to_time = time(5, 0)
        data = {
            "monday": setting.monday,
            "tuesday": setting.tuesday,
            "wednesday": setting.wednesday,
            "thursday": setting.thursday,
            "friday": setting.friday,
            "saturday": setting.saturday,
            "sunday": setting.sunday,
            "from_time": setting.from_time,
            "to_time": setting.to_time,
        }
        form = SleepSettingsForm(data=data)
        self.assertFalse(form.is_valid())
