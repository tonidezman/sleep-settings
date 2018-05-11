import json
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views.generic import View
import os

from dashboard.models import SleepSetting

def get_sleep(request):
    data = json.dumps({ 'shouldSleep': SleepSetting.should_sleep() })
    return HttpResponse(data, content_type='application/json')


class ReactAppView(View):

    def get(self, request):
        try:

            with open(os.path.join(settings.REACT_APP, 'build', 'index.html')) as file:
                return HttpResponse(file.read())

        except :
            return HttpResponse(
                """
                index.html not found ! build your React app !!
                """,
                status=501,
            )