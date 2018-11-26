from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class BlogType(models.Model):
    """ 博客类型(分类)"""
    type_name = models.CharField('分类', max_length=12)
    
    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return  self.type_name

class Blog(models.Model):
    """ 博客(文章)"""
    title = models.CharField('标题', max_length=30)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING, verbose_name='分类')
    content = RichTextUploadingField('内容')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')
    readed_num = models.IntegerField(default=0, verbose_name='阅读计数')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_updated_time = models.DateTimeField('最后修改时间', auto_now=True)
    
    class Meta:
        verbose_name = "博客"
        verbose_name_plural = verbose_name
        ordering = ['-created_time']
    
    def __str__(self):
        # return "<Blog: %s>" % self.title
        return self.title
