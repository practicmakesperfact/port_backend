from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured', 'order', 'created_at', 'updated_at']
    list_filter = ['is_featured', 'created_at', 'updated_at']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_featured']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'icon', 'image')
        }),
        ('Links', {
            'fields': ('github_url', 'live_url')
        }),
        ('Technical Details', {
            'fields': ('tech_stack', 'features')
        }),
        ('Settings', {
            'fields': ('is_featured', 'order')
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related()
