from django.contrib import admin
from .models import DataSkill

class DataSkillModelAdmin(admin.ModelAdmin):
    list_display = ["dataskill", "percentage"]
    class Meta:
        model = DataSkill

admin.site.register(DataSkill, DataSkillModelAdmin)