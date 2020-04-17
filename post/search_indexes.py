#!usr/bin/python
# -*- coding:utf-8 -*-
# __author = 'Bruce.张'

from haystack import indexes
from post.models import *

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    title = indexes.NgramField(model_attr='title')
    content = indexes.NgramField(model_attr='content')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-created')

