# vim:fileencoding=utf-8
import json
from datetime import datetime
import math
import random
from django import template
from django.template import Template, Context
import re
import time

from django.template.loader import render_to_string

from cms_plugins.models import Block

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
    return int(value) + int(arg)


def multiply(value, arg):
    return int(value) * int(arg)


def split(values, arg):
    n = values.split(arg)
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


TAGS = {'block':
        {'model': Block, 'template': 'utils/render/render-block.html'},
        }


def render_tags(value):
    t = re.findall('{\$ \w+-\d+ \$}', value)
    from itertools import chain
    tags = list(chain(t, re.findall('{\$ \w+-\d+ \w+ \$}', value)))
    result = []
    for i in tags:
        try:
            name, id = (re.findall('\w+-\d+', i))[0].split('-')
            result.append(
                [i, render_to_string(TAGS[name]['template'], {'obj': TAGS[name]['model'].objects.get(id=int(id))})])
        except:
            result.append([i, ''])
    for res in result:
        value = value.replace(res[0], res[1])
    return value


def delete_tags(value):
    t = re.findall('{\$ \w+-\d+ \$}', value)
    from itertools import chain
    tags = list(chain(t, re.findall('{\$ \w+-\d+ \w+ \$}', value)))
    for res in tags:
        value = value.replace(res, '')
    return value


def delim(value, arg):
    return math.ceil(float(value)/float(arg))


register.filter('render_tags', render_tags)
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
