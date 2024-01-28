from django.contrib import admin
from .models import (
    Home,
    Subject,
    About,
    Partners,
)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    search_fields = ('title',)
    list_display_links = ('title',)


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name',)
    list_display_links = ('name',)
    filter_horizontal = ('subject',)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name',)
    list_display_links = ('name', 'last_name',)
    hiring_date_hierarchy = 'date_of_birth'


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('id', )

