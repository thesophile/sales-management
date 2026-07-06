
from django.urls import path, include
from admin_side import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.admin, name='admin'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit/<int:id>/', views.edit_product, name='edit_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)