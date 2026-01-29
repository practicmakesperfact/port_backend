from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('data/', views.profile_data, name='profile_data'),
]
