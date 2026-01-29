from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
    
    actions = ['mark_as_read']
    
    def mark_as_read(self, request, queryset):
        """Mark selected messages as read"""
        count = queryset.count()
        for message in queryset:
            message.mark_as_read()
        self.message_user(request, f'{count} messages marked as read.')
    mark_as_read.short_description = 'Mark selected messages as read'
