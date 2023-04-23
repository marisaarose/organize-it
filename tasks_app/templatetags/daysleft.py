from django import template 
from datetime import date 
from django.conf import settings

register = template.Library()

@register.filter
def days_left(value):
    now = date(date.today().year, date.today().month, date.today().day)
    future = date(value.year, value.month, value.day)
    delta = future - now
    if delta.days < 0:
        return 'Overdue'
    if delta.days == 0:
        return ' today'
    return str(delta.days) + ' days left'