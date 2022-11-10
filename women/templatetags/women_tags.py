from django import template
from women.models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if filter:
        return Category.objects.filter(pk=filter)
    else:
        return Category.objects.all()


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if sort:
        cats = Category.objects.order_by(sort)
    else:
        cats = Category.objects.all()
    return {"cats": cats, 'cat_selected': cat_selected}
