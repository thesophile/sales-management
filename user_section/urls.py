
from django.urls import path, include
from user_section import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('enquiry/<int:product_id>/', views.enquiry_form, name='enquiry_form'),
    path('enquiry/success/', views.enquiry_success, name='enquiry_success'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)