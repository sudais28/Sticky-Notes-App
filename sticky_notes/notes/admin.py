from django.contrib import admin
from .models import Note

# 1. Customize the branding
admin.site.site_header = "Sticky Note Board Admin"
admin.site.site_title = "Board Admin Portal"
admin.site.index_title = "Welcome to the Board Management Panel"

# 2. Register the Note model with a custom interface
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    # What columns to show in the list
    list_display = ('title', 'user', 'category', 'priority', 'is_completed', 'created_at')
    
    # What to allow searching for
    search_fields = ('title', 'content', 'user__username')
    
    # What filters to show on the right sidebar
    list_filter = ('category', 'priority', 'is_completed', 'created_at')
    
    # Organize fields in the editor
    fieldsets = (
        ('Content', {
            'fields': ('title', 'content', 'user')
        }),
        ('Metadata', {
            'fields': ('category', 'priority', 'color', 'is_completed')
        }),
    )

    # Automatically set the user to the logged-in user when creating via admin
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
        super().save_model(request, obj, form, change)
