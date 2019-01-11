from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
     This cut out all value of "arg" from string
    """
    return value.replace(arg,'')

#register.filter('cut', cut)
