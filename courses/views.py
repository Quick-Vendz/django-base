from django.shortcuts import render
from .models import Course, Category

def course_list(request):
    categories = Category.objects.all()
    courses = Course.objects.all()
    
    # Filter by level
    level = request.GET.get('level')
    if level:
        courses = courses.filter(level=level)
    
    context = {
        'categories': categories,
        'courses': courses,
        'selected_level': level,
    }
    return render(request, 'courses/base/course_list.html', context)


def course_detail(request, slug):
    course = Course.objects.get(slug=slug)
    context = {
        'course': course,
    }
    return render(request, 'courses/base/course_detail.html', context)