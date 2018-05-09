import json
from django.shortcuts import render
from django.http import HttpResponse

from dashboard.models import SleepSetting

def get_sleep(request):
    data = json.dumps({ 'shouldSleep': SleepSetting.should_sleep() })
    return HttpResponse(data, content_type='application/json')
