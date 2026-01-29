from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/profile/', include('profiles.urls')),
    path('api/skills/', include('skills.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/contact/', include('contact.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
