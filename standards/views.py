from django.shortcuts import render
from data.models import Category

def home(request):
    selected_category = request.GET.get('category', None)
    
    if selected_category:
        categories = Category.objects.filter(slug=selected_category)
    else:
        categories = Category.objects.all()
        

    standards_by_category = {}
    for category in categories:
        standards = category.standards.all()
        standards_by_category[category] = standards
    
    context = {
        'categories': categories,
        'standards_by_category': standards_by_category,
    }   
    return render(request, 'standards/base/home.html', context)
