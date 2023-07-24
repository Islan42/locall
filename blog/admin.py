from django.contrib import admin
from .models import BlogPost, BlogAuthor, BlogComment

# Register your models here.
# admin.site.register(BlogPost)
admin.site.register(BlogAuthor)
# admin.site.register(BlogComment)

class BlogCommentInline(admin.TabularInline):
    model = BlogComment
    extra = 0

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    inlines = [BlogCommentInline]

@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['truncate_str']
    