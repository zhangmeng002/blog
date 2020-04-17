import math
from django.shortcuts import render

# Create your views here.
#渲染主页面
from post.models import Post, Category
from django.core.paginator import Paginator

def queryall(request, num=1):

    num = int(num)
    #获取所有的帖子信息
    postlist = Post.objects.all().order_by('-created')
    #创建分页器对象
    pager = Paginator(postlist, 1)
    #获取当前页数据
    perpagelist = pager.page(num)

    #生成页码数列表
    #每页开始页码
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1

    #每页结束页码
    end = begin + 9
    if end > pager.num_pages:
        end = pager.num_pages
    if end <= 10:
        begin = 1
    else:
        begin = end - 9

    pagelist = range(begin, end+1)

    return render(request, 'index.html', {'postlist': perpagelist, 'pagelist': pagelist, 'currentnum': num})

#阅读全文
def detail(request, post_id):
    post = Post.objects.get(id=post_id)

    return render(request, 'detail.html', locals())


def cateshow(request, cate_id):
    # cate = Category.objects.get(id=cate_id)
    posts = Post.objects.filter(category_id=cate_id)
    return render(request, 'article.html', {'posts': posts})


def bycreated(request, year, month):
    posts = Post.objects.filter(created__year=year, created__month=month)

    # print(posts)
    return render(request, 'article.html', {'posts': posts})
  