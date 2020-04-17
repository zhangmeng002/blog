from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=32, unique=True, verbose_name='类别名称')
    class Meta:
        db_table = 't_category'
        verbose_name = '类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cname

class Tag(models.Model):
    tname = models.CharField(max_length=32, unique=True, verbose_name='标签名称')
    class Meta:
        db_table = 't_tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.tname

class Post(models.Model):
    title = models.CharField(max_length=128, unique=True, verbose_name='标题')
    desc = models.CharField(max_length=128)
    content = RichTextUploadingField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    class Meta:
        db_table = 't_post'
        verbose_name = '帖子'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

