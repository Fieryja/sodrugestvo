# vim:fileencoding=utf-8
import json
from datetime import datetime
import math
import random
from django import template
import re

register = template.Library()

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


def parse_int(value):
    return int(value)


def parse_str(value):
    return str(value)


def parse_float(value):
    e, f = str(value).split('.')
    if int(f) > 0:
        return value
    return int(e)


def replace(value, param):
    f, e = param.split('#')
    try:
        value = str(value).replace(f, e)
    except:
        value = value.replace(f, e)
    return value


register.filter('split_line', split_line)
register.filter('str', parse_str)
register.filter('parse_int', parse_int)
register.filter('split', split)
register.filter('multiply', multiply)
register.filter('plus', plus)
register.filter('minus', minus)
