from django.shortcuts import render
from django.http import JsonResponse
from .models import Project

def projects_data(request):
    projects = Project.objects.filter(is_featured=True).order_by('order', '-created_at')
    data = []
    
    for project in projects:
        data.append({
            'id': project.id,
            'title': project.title,
            'description': project.description,
            'icon': project.icon,
            'image': project.image.url if project.image else None,
            'github_url': project.github_url,
            'live_url': project.live_url,
            'tech_stack': project.get_tech_stack_list(),
            'features': project.get_features_list(),
        })
    
    return JsonResponse({'projects': data})
