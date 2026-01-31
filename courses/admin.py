from django.contrib import admin
from .models import Course, Category, SubCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)
    
    
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'subcategory', 'teacher', 'is_published', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('level', 'subcategory', 'is_published', 'created_at', 'updated_at')
    ordering = ('level', 'title')
    
