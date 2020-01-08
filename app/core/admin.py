from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ['email', 'name']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal Info'), {'fields': ('name',)}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (('Important dates'), {'fields': ('last_login',)}))
    # Page for adding new users
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2')}),)


class DataSkillModelAdmin(admin.ModelAdmin):
    list_display = ["dataskill", "percentage"]

    class Meta:
        model = models.DataSkill


admin.site.register(models.User, UserAdmin)
admin.site.register(models.MyProfile)
admin.site.register(models.DataSkill, DataSkillModelAdmin)
