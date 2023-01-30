from django import template
from coolsite.women.models import *

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()
