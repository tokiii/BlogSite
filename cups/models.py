from django.db import models
from django.contrib.auth.models import User


class BlogType(models.Model):
    type_name = models.CharField(max_length=15, verbose_name="标题")

    def __str__(self):
        return self.type_name


# verbose_name 后台可以显示中文标题
class Blog(models.Model):
    title = models.CharField(max_length=32, verbose_name="博客标题")
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING, verbose_name="博客类型")
    content = models.TextField(verbose_name="博客内容")
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="博客作者")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    last_update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return "<Blog %s>" % self.title
