from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from site_app.views import home

urlpatterns = [
    path(r'', home, name='homepage'),
    path('tinymce/', include('tinymce.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
