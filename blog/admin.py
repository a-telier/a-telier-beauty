from django.contrib import admin
from .models import Article, Blog_category

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('blog_category', 'title', 'url', 'created_on')
    # list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'url': ('title',)}
  
class CategoryAdmin (admin.ModelAdmin):
    list_display = (
        'name',
        'display_name',
    )

admin.site.register(Article, ArticleAdmin)
admin.site.register(Blog_category, CategoryAdmin)