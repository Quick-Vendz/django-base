from django.contrib import admin
from .models import LearningArea, Strand, NZCExpectation


@admin.register(LearningArea)
class LearningAreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    
    
@admin.register(Strand)
class StrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'learning_area', 'description')
    list_filter = ('learning_area',)
    search_fields = ('name', 'learning_area__name')
    
    
@admin.register(NZCExpectation)
class NZCExpectationAdmin(admin.ModelAdmin):
    list_display = ('strand', 'phase', 'year_level', 'expectation_text')
    list_filter = ('phase', 'year_level', 'strand__learning_area')
    search_fields = ('expectation_text', 'strand__name', 'strand__learning_area__name')
    ordering = ('strand', 'phase', 'year_level')
    


