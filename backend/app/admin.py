from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_staff', 'get_groups')

    def get_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])
    get_groups.short_description = 'Groupes'

    def get_queryset(self, request):
        print(f"[DEBUG] CustomUserAdmin active pour {request.user}")
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Optionnel : masquer les users staff si tu veux
        return qs

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj and obj.is_staff:
            return False
        return super().has_delete_permission(request, obj)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.is_superuser:
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
