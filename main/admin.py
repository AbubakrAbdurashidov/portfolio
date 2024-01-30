from django.contrib import admin
from .models import (
    Home,
    Subject,
    About,
    Partner,
    Education,
    Experience,
    TopSkill,
    Skill,
    Award,
    Service,
    Category,
    Project,
    Counter,
    Contact,
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


@admin.register(Partner)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('id', )


@admin.register(Education)
class EducationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'university_name',)
    list_display_links = ('university_name',)
    date_hierarchy = 'start_date'


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name',)
    list_display_links = ('company_name',)
    date_hierarchy = 'start_date'


@admin.register(TopSkill)
class TopSkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('title',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('title',)


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('id', 'award_name',)
    list_display_links = ('award_name',)
    date_hierarchy = 'date'


@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)


@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('title',)
    # filter_horizontal = ('category',)


@admin.register(Counter)
class CounterAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date',)
    readonly_fields = ('created_date',)
    date_hierarchy = 'created_date'
    list_display_links = ('created_date',)


