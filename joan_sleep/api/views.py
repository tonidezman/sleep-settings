from django.shortcuts import render
from django.http import HttpResponse
import json

def get_sleep(request):
    data = json.dumps({ 'shouldSleep': False })
    return HttpResponse(data, content_type='application/json')
