from django import template

register = template.Library()

@register.filter(is_safe=True)
def fb(rand):
    r = int(rand)
    if r%15 == 0:
        return "BizzFuzz"
    elif r%5 == 0:
        return "Fuzz"
    elif r%3 == 0:
        return "Bizz"
    else:
        return ""
