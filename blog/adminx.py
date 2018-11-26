from django.contrib import admin

# pip install git+https://github.com/sshwsfc/xadmin.git@django2

import xadmin
from xadmin import views
from import_export import resources
from .models import BlogType, Blog


class BlogTypeAdmin(object):
    list_display = ['id', 'type_name']
    model_icon = 'fa fa-tags'
    
    

class BlogResource(resources.ModelResource):
    class Meta:
        model = Blog
        # fields = ('name', 'description',)
        # exclude = ()

# @xadmin.sites.register(Blog)
# 插件导入导出功能
# class FooAdmin(object):
#     import_export_args = {'import_resource_class': BlogResource, 'export_resource_class': BlogResource}

@xadmin.sites.register(Blog)
class BlogAdmin(object):
    list_display = ('title', 'blog_type', 'author', 'readed_num', 'created_time', 'last_updated_time',) #列表字段
    readonly_fields = ['readed_num']
    list_editable = ['title', 'blog_type',] # 快速编辑
    list_display_links = ('title',) #点击进入编辑界面的字段
    list_per_page = 15 # list_per_page设置每页显示多少条记录，默认是100条
    search_fields = ['title', 'content'] #搜索字段
    list_filter = ['title', 'blog_type', 'created_time'] #过滤器字段
    model_icon = 'fa fa-book' #图标
    list_export = ('xls',) # xadmin 自带导出文件类型
    import_export_args = {'import_resource_class': BlogResource, } #'export_resource_class': BlogResource



# 基本的修改
class BaseSetting(object):
    enable_themes = True   # 打开主题功能
    use_bootswatch = True  #

# 针对全局的
class GlobalSettings(object):
    site_title = "坤子的博客后台"  # 系统名称
    site_footer = "2018 xuyukun.com" # 底部版权栏
    # menu_style = "accordion"     # 将菜单栏收起来

    
    
# xadmin后台注册model
xadmin.site.register(BlogType, BlogTypeAdmin)
# xadmin.site.register(Blog, BlogAdmin)

# 注册，注意一个是BaseAdminView，一个是CommAdminView
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)