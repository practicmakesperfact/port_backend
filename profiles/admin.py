from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'years_experience', 'projects_delivered', 'happy_clients', 'has_profile_image', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'title', 'bio']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Profile Picture', {
            'fields': ('profile_image',),
            'description': 'Upload a professional profile picture. Recommended size: 400x400px. Max file size: 5MB.'
        }),
        ('Basic Information', {
            'fields': ('name', 'title')
        }),
        ('Biography', {
            'fields': ('bio', 'detailed_bio'),
            'description': 'Tell visitors about yourself and your expertise.'
        }),
        ('Statistics', {
            'fields': ('years_experience', 'projects_delivered', 'happy_clients'),
            'description': 'Your professional achievements and experience.'
        }),
        ('Social Links', {
            'fields': ('github_url', 'linkedin_url', 'upwork_url'),
            'description': 'Link to your professional social media profiles.'
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    
    def has_profile_image(self, obj):
        return bool(obj.profile_image)
    has_profile_image.boolean = True
    has_profile_image.short_description = 'Has Image'
    
    def has_add_permission(self, request):
        # Only allow one profile instance
        return not Profile.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of the profile
        return False
