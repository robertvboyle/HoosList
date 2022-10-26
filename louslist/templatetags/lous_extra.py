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

    weekdays = ["MoTuWeThFr","MoWeFr","MoTu", "MoWe", "MoTh", "MoFr", "TuWe","TuTh","TuFr", "TuThFr", "WeTh","WeFr", "ThFr", "Mo", "Tu", "We", "Th", "Fr", "Sa", "-"]
    classType = ["LEC", "SEM", "DIS", "LAB", "IND", "SPS", "PRA", "WKS", "STO", "CLN"]

    return sorted(value, key=lambda valdict: (classType.index(valdict["component"]), weekdays.index(valdict["meetings"][0]["days"]), valdict["meetings"][0]["start_time"]))
