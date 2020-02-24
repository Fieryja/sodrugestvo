# vim:fileencoding=utf-8
import json
from datetime import datetime
import math
import random
from django import template
from django.db.models import Count
from django.template import Template, Context
import re

register = template.Library()


def render_field(val, arg):
    t = Template(val)
    c = Context({'item': arg})
    return t.render(c)


def stringToID(val):
    return int(val.split('-')[1].split(' ')[0])


def minus(value, arg):
    return value - int(arg)


def plus(value, arg):
    return float(value) + float(arg)


def multiply(value, arg):
    return float(value) * float(arg)


def split(values, arg):
    n = values.split(arg)
    return n


def split_line(values):
    n = values.split('\r\n')
    return n


def replace_unicode(value):
    import re
    r = re.sub(r'&([A-Za-z]+);', '', value)
    return r


def parse_int(value):
    return int(value)


def get_date(value):
    return datetime.strptime(value, '%a, %d %b %Y %H:%M:%S %Z')


def files(values):
    n = int(math.floor(values / 2.00))
    return n


def parse_str(value):
    return str(value)


def price_format(value):
    decimal_points = 3
    separator = u' '
    value = str(value)
    if len(value) <= decimal_points:
        return value
    parts = []
    while value:
        parts.append(value[-decimal_points:])
        value = value[:-decimal_points]
    parts.reverse()
    return separator.join(parts)


def to_class_name(value):
    return value.__class__.__name__


def sizes(value, arg):
    e = random.randint(int(arg.split(',')[0]), int(arg.split(',')[1]))
    return e


def parse_float(value):
    e, f = str(value).split('.')
    if int(f) > 0:
        return value
    return int(e)


def get_extension(value):
    f = str(value).split('.')
    return f[-1]


def get_arr_el(arr, id):
    return arr[id]


def get_dict_el(dict, key):
    if isinstance(dict, str):
        dict = json.loads(dict)
    return dict.get(key)


def is_entry(value, arg):
    if re.findall(arg, value) != 0:
        return True
    return False


def replace(value, param):
    f, e = param.split('#')
    try:
        value = str(value).replace(f, e)
    except:
        value = value.replace(f, e)
    return value


def die_ie(value):
    arr = ['MSIE 8', 'MSIE 7', 'MSIE 6']
    if len([i for i in arr if i in value]) > 0:
        return False
    return True


def delim(value, arg):
    return math.ceil(float(value) / float(arg))


def by_date(objects):
    from django.db.models.functions import TruncMonth
    from contents.models import Event
    month = objects.annotate(month=TruncMonth('date')).values_list('month', flat=True)
    result = {}
    from django.template.defaultfilters import date
    for i in month:
        result.update({date(i, 'F Y'): Event.objects.filter(id__in=objects.values_list('id', flat=True)).filter(
            date__date__month=i.month, date__date__year=i.year).order_by('date')})
    return result


register.assignment_tag(by_date)
register.filter('split_line', split_line)
register.filter('render_field', render_field)
register.filter('delim', delim)
register.filter('die_ie', die_ie)
register.filter('replace', replace)
register.filter('is_entry', is_entry)
register.filter('get_extension', get_extension)
register.filter('get_arr_el', get_arr_el)
register.filter('parse_float', parse_float)
register.filter('sizes', sizes)
register.filter('get_dict_el', get_dict_el)
register.filter('to_class_name', to_class_name)
register.filter('price', price_format)
register.filter('files', files)
register.filter('parse_date', get_date)
register.filter('str', parse_str)
register.filter('parse_int', parse_int)
register.filter('replace_unicode', replace_unicode)
register.filter('split', split)
register.filter('multiply', multiply)
register.filter('plus', plus)
register.filter('minus', minus)
