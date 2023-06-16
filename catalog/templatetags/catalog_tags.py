from django import template
from catalog.models import *
from config import settings

register = template.Library()


@register.simple_tag()
def mediapath(image_path):
    return image_path
