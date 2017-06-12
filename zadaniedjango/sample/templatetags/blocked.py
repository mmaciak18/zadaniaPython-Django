from django import template
from datetime import date
from dateutil.relativedelta import relativedelta

register = template.Library()

@register.filter(is_safe=True)
def blocked(born):
    if born + relativedelta(years=13) > date.today():
        return "Blocked"
    else:
        return "Allowed"
