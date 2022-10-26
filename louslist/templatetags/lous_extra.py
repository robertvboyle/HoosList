from django import template
from django.template.defaultfilters import stringfilter
from datetime import datetime

register = template.Library()

@register.filter(name='convertTime')
@stringfilter
def convertTime(value):
    if value != "":
        arr = value.split(".")
        firstTime = arr[0]+":"+arr[1]
        firstTime = datetime.strptime(firstTime, "%H:%M")
        return str(firstTime.strftime("%I:%M %p"))
    return value

# 

@register.filter(name='sortMeeting')
def sortMeeting(value):
    weekdays = ["MoWeFr","MoWe", "MoFr", "TuTh", "Mo", "Tu", "We", "Th", "Fr", "-"]
    r = sorted(value, key=lambda valdict: ([-ord(c) for c in valdict["component"]], weekdays.index(valdict["meetings"][0]["days"]), valdict["meetings"][0]["start_time"] ))
    print(r)

    return r

