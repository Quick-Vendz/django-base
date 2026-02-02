from django.contrib import admin
from .models import Standard

@admin.register(Standard)
class StandardAdmin(admin.ModelAdmin):
    list_display = ('standard_number', 'title', 'level', 'credits', 'assessment_type', 'mode', 'version', 'status', 'created_at', 'updated_at')
    search_fields = ('standard_number', 'title')
    list_filter = ('level', 'assessment_type', 'mode', 'status')
    ordering = ('standard_number',)
