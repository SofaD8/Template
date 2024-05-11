from django.contrib import admin
from .models import Services, Portfolio, About, Team, Contact
from django.utils.safestring import mark_safe

# Register your models here.
admin.site.register(Contact)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_visible', 'sort')
    list_editable = ('description', 'is_visible', 'sort')
    list_filter = ('is_visible',)
    search_fields = ('name',)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'name', 'description', 'is_visible', 'sort')
    list_editable = ('description', 'name', 'is_visible', 'sort')
    list_filter = ('is_visible',)
    search_fields = ('name',)

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=50 height=50>')

    photo_src_tag.short_description = 'Portfolio photo'

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'name', 'description', 'is_visible', 'sort')
    list_editable = ('description', 'is_visible', 'sort')
    list_filter = ('is_visible',)
    search_fields = ('name',)

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=50 height=50>')

    photo_src_tag.short_description = 'About photo'

    @admin.register(Team)
    class TeamAdmin(admin.ModelAdmin):
        list_display = ('photo_src_tag', 'name', 'description', 'is_visible', 'sort')
        list_editable = ('description', 'is_visible', 'sort')
        list_filter = ('is_visible',)
        search_fields = ('name',)

        def photo_src_tag(self, obj):
            if obj.photo:
                return mark_safe(f'<img src="{obj.photo.url}" width=50 height=50>')

        photo_src_tag.short_description = 'Team photo'


