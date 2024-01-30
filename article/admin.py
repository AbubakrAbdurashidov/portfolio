from django.contrib import admin
from .models import (
    Author,
    Category,
    Tag,
    Article,
    SubArticle,
    Comment,
)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('title',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('title',)


class SubArticleAdmin(admin.TabularInline):
    model = SubArticle
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [SubArticleAdmin]
    list_display = ('id', 'title',)
    search_fields = ('author', 'category',)
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)
    list_display_links = ('title',)
    filter_horizontal = ('tags',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'name', 'email', 'get_image', 'created_date', )
    search_fields = ('name', 'article__title')
    readonly_fields = ('created_date',)
    autocomplete_fields = ('article',)