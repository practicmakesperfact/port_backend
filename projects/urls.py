from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('data/', views.projects_data, name='projects_data'),
]
