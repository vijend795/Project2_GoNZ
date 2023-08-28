from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

# Register your models here.
# Extend the UserAdmin class
class CustomUserAdmin(UserAdmin):
    

    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('position', 'department','user_image')}),
    )
    list_display = ('id', 'get_full_name','username', 'email', 'position', 'department','display_groups','user_image')  # Add 'get_full_name' to display combined name
    list_filter = UserAdmin.list_filter + ('position', 'department')  # Add 'position' and 'department' to filters

    # Custom method to get combined first name and last name
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    get_full_name.short_description = 'Full Name'  # Column header in admin

    def display_groups(self, obj):
        return format_html(', '.join([group.name for group in obj.groups.all()]))
    display_groups.short_description = 'Groups'  # Column header in admin

# Register the NewUser model with the custom admin class
admin.site.register(NewUser, CustomUserAdmin)