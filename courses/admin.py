from django.contrib import admin
from .models import Course, Category, Block

@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'estimated_weeks')
    search_fields = ('title', 'description')
    list_filter = ('course',)
    ordering = ('course', 'title')
    



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'teacher', 'is_published', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('level', 'is_published', 'created_at', 'updated_at')
    ordering = ('level', 'title')
    
