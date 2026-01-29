from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import ContactMessage

@csrf_exempt
@require_http_methods(["POST"])
def submit_contact(request):
    """Handle contact form submission"""
    try:
        # Parse JSON data
        data = json.loads(request.body)
        
        # Validate required fields
        required_fields = ['name', 'email', 'subject', 'message']
        for field in required_fields:
            if not data.get(field):
                return JsonResponse({
                    'success': False,
                    'error': f'{field} is required'
                }, status=400)
        
        # Create contact message
        contact_message = ContactMessage.objects.create(
            name=data['name'],
            email=data['email'],
            subject=data['subject'],
            message=data['message']
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Your message has been sent successfully!'
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid data format'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': 'An error occurred while sending your message'
        }, status=500)
