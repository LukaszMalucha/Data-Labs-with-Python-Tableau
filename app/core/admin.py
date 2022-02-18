from django.contrib import admin

from core import models


class DataSkillModelAdmin(admin.ModelAdmin):
    list_display = ["dataskill", "percentage"]

    class Meta:
        model = models.DataSkill


admin.site.register(models.MyProfile)
admin.site.register(models.DataSkill, DataSkillModelAdmin)
