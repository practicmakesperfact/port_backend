from django.urls import path
from . import views

app_name = 'skills'

urlpatterns = [
    path('data/', views.skills_data, name='skills_data'),
]
