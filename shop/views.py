from django.utils import timezone
from django.http import HttpResponse
from datetime import datetime, timedelta

from django.shortcuts import render


# Create your views here.
def index(request):
    now = timezone.now()
    tz = timezone.get_current_timezone()
    timezone_name = tz.tzname(now)
    return HttpResponse(now.__str__() + " " + timezone_name)


def future(request):
    future = datetime.now() + timedelta(days=500)
    day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return HttpResponse(future.__str__() + " " + day[future.weekday()])
