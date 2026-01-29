from django.contrib import admin
from .models import SkillCategory, Skill

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'order', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description']
    list_editable = ['order']
    ordering = ['order']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'icon', 'is_active', 'order', 'created_at']
    list_filter = ['category', 'is_active', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['category', 'order']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'icon', 'is_active')
        }),
        ('Details', {
            'fields': ('description', 'order')
        }),
    )
