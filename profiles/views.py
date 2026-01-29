from django.shortcuts import render
from django.http import JsonResponse
from .models import Profile

def profile_data(request):
    profile = Profile.objects.first()
    if profile:
        data = {
            'name': profile.name,
            'title': profile.title,
            'bio': profile.bio,
            'detailed_bio': profile.detailed_bio,
            'profile_image': profile.profile_image.url if profile.profile_image else None,
            'years_experience': profile.years_experience,
            'projects_delivered': profile.projects_delivered,
            'happy_clients': profile.happy_clients,
            'github_url': profile.github_url,
            'linkedin_url': profile.linkedin_url,
            'upwork_url': profile.upwork_url,
        }
    else:
        # Default data if no profile exists
        data = {
            'name': 'Haymanot Asmare',
            'title': 'Full Stack Software Engineer',
            'bio': 'I\'m a passionate Full Stack Software Engineer with extensive experience in building scalable web applications and creating exceptional digital experiences.',
            'detailed_bio': 'I specialize in transforming complex business requirements into elegant, efficient solutions that drive measurable results.',
            'profile_image': None,
            'years_experience': 5,
            'projects_delivered': 50,
            'happy_clients': 30,
            'github_url': 'https://github.com',
            'linkedin_url': 'https://linkedin.com',
            'upwork_url': 'https://upwork.com',
        }
    
    return JsonResponse(data)
