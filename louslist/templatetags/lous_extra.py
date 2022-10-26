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

