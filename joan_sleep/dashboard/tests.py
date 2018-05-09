import datetime
from unittest.mock import patch
from django.test import TestCase
from django.utils import timezone

from dashboard.models import SleepSetting

class SleepSettingTest(TestCase):
    def setUp(self):
        setting = SleepSetting()
        setting.monday = True
        setting.thursday = True
        setting.saturday = True
        setting.from_time = '07:00'
        setting.to_time = '19:00'
        setting.save()

    def tearDown(self):
        SleepSetting.objects.all().delete()

    def test_false_when_device_is_awake(self):
        with patch.object(timezone, 'now', return_value=datetime.datetime(2018, 5, 10, 11, 00)) as mock_now:
            self.assertEqual(SleepSetting.should_sleep(), False)

    def test_datetime_for_the_same_date_but_little_earlier_as_in_settings(self):
        with patch.object(timezone, 'now', return_value=datetime.datetime(2018, 5, 10, 5, 00)) as mock_now:
            self.assertEqual(SleepSetting.should_sleep(), "2018-05-10T07:00-19:00")

    def test_datetime_for_the_same_date_but_little_later_as_in_settings(self):
        with patch.object(timezone, 'now', return_value=datetime.datetime(2018, 5, 10, 22, 00)) as mock_now:
            self.assertEqual(SleepSetting.should_sleep(), "2018-05-12T07:00-19:00")

    def test_datetime_for_the_same_date_but_little_later_as_in_settings_next_week(self):
        setting = SleepSetting.objects.first()
        setting.monday = False
        setting.thursday = True
        setting.saturday = False
        setting.save()
        with patch.object(timezone, 'now', return_value=datetime.datetime(2018, 5, 10, 22, 00)) as mock_now:
            self.assertEqual(SleepSetting.should_sleep(), "2018-05-17T07:00-19:00")

    def test_datetime_object_until_device_should_be_asleep(self):
        with patch.object(timezone, 'now', return_value=datetime.datetime(2018, 5, 8, 11, 00)) as mock_now:
            self.assertEquals(SleepSetting.should_sleep(), "2018-05-10T07:00-19:00")

    def test_datetime_object_until_device_should_be_asleep_into_next_week(self):
        with patch.object(timezone, 'now', return_value=datetime.datetime(2018, 5, 13, 12, 00)) as mock_now:
            self.assertEquals(SleepSetting.should_sleep(), "2018-05-14T07:00-19:00")