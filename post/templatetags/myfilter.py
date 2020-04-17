#!usr/bin/python
# -*- coding:utf-8 -*-
# __author = 'Bruce.张'

from django.template import Library

register = Library()

@register.filter
def md(value):
    import markdown
    return markdown.markdown(value)