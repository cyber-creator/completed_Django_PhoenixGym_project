from django.contrib import admin
from .models import Blog, BlogCategory, Contact

# Register your models here.
admin.site.register(Contact)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


# class ArticleAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}
#
#
# @admin.register(Track)
# class TrackAdmin(admin.ModelAdmin):
#     list_display = ('title','artist')
