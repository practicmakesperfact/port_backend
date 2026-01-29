from django.shortcuts import render
from django.http import JsonResponse
from .models import SkillCategory, Skill

def skills_data(request):
    categories = SkillCategory.objects.prefetch_related('skills').all()
    data = []
    
    for category in categories:
        skills_list = []
        for skill in category.skills.filter(is_active=True):
            skills_list.append({
                'name': skill.name,
                'icon': skill.icon,
                'description': skill.description,
            })
        
        data.append({
            'id': category.id,
            'name': category.name,
            'icon': category.icon,
            'description': category.description,
            'skills': skills_list
        })
    
    return JsonResponse({'categories': data})
