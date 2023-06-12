from django import template
from catalog.models import *

register = template.Library()


@register.simple_tag()
def mediapath():
    return r'/Users/olgaaros/Desktop/PY_SkyPro/C6_Django/19.1_19.2/HW20/media'