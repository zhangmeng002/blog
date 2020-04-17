#!usr/bin/python
# -*- coding:utf-8 -*-
# __author = 'Bruce.张'
from django.db import connection
from django.db.models import Count

from post.models import Post

#自定义全局上下文
def getRightInfo(request):
    #获取分类信息
    r_catepost = Post.objects.values('category__cname', 'category').annotate(c=Count('*')).order_by('-c')
    #近期文章排序
    r_recpost = Post.objects.all().order_by('-created')[:3]
    #获取日期归档信息
    cursor = connection.cursor()
    #mysql日期转为字符串
    cursor.execute('select created,count("*") c from t_post group by date_format(created,"%Y-%m") order by c,created desc')
    r_file_post = cursor.fetchall()
    # print(r_file_post)
    return {'r_catepost': r_catepost, 'r_recpost': r_recpost, 'r_file_post': r_file_post}
