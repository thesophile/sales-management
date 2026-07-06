
from django.urls import path, include
from user_section import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('user_section/', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)