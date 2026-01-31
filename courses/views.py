from django.shortcuts import render
from .models import Course, Category, SubCategory

def course_list(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    courses = Course.objects.all()
    
    # Filter by subcategory
    subcategory_id = request.GET.get('subcategory')
    if subcategory_id:
        courses = courses.filter(subcategory_id=subcategory_id)
    
    # Filter by level
    level = request.GET.get('level')
    if level:
        courses = courses.filter(level=level)
    
    # Group courses by category
    courses_by_category = {}
    for category in categories:
        courses_by_category[category.name] = courses.filter(subcategory__category=category)
    
    context = {
        'categories': categories,
        'subcategories': subcategories,
        'courses_by_category': courses_by_category,
        'selected_level': level,
    }
    return render(request, 'courses/base/course_list.html', context)


def course_detail(request, slug):
    course = Course.objects.get(slug=slug)
    context = {
        'course': course,
    }
    return render(request, 'courses/base/course_detail.html', context)