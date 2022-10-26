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


@register.filter(name='sortMeeting')
def sortMeeting(value):
    for i in range(len(value)):
        if value[i]["meetings"] == []:
            value[i]["meetings"] = [{'days': '-', 'start_time': '', 'end_time': '', 'facility_description': '-'}]

    weekdays = ["MoWeFr","MoWe", "MoFr", "TuTh", "WeFr", "Mo", "Tu", "We", "Th", "Fr", "-"]
    classType = ["LEC", "DIS", "LAB", "IND", "SPS"]

    return sorted(value, key=lambda valdict: (classType.index(valdict["component"]), weekdays.index(valdict["meetings"][0]["days"]), valdict["meetings"][0]["start_time"]))
