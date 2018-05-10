from django.test import TestCase

from dashboard.models import SleepSetting

class APIViewTest(TestCase):
    def setUp(self):
        setting = SleepSetting()
        setting.monday = True
        setting.save()

    def test_get_sleep_url(self):
        res = self.client.get("/getSleep/")
        self.assertEqual(res.status_code, 200)
