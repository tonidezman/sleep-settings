from django.test import TestCase

from dashboard.models import SleepSetting

class DashBoardViewTest(TestCase):
    def setUp(self):
        setting = SleepSetting()
        setting.monday = True
        setting.save()

    def test_dashboard_settings_url(self):
        res = self.client.get("/dashboard/settings/")
        self.assertEqual(res.status_code, 200)

    def test_get_sleep_url(self):
        res = self.client.get("/getSleep/")
        self.assertEqual(res.status_code, 200)