
from django.urls import path, include, reverse_lazy
from admin_side import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.admin, name='admin'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit/<int:id>/', views.edit_product, name='edit_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    path('admin-login/', auth_views.LoginView.as_view(template_name='admin_side/login.html'), name='admin_login'),
    path('admin-logout/', auth_views.LogoutView.as_view(next_page='admin_login'), name='admin_logout'),
    
    
    path('admin-change-password/', auth_views.PasswordChangeView.as_view(
        template_name='admin_side/change_password.html',
        success_url=reverse_lazy('password_change_done')
    ), name='admin_change_password'),

    path('admin-change-password/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='admin_side/change_password_done.html'
    ), name='password_change_done'),
    
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/edit/<int:id>/', views.edit_category, name='edit_category'),
    path('categories/delete/<int:id>/', views.delete_category, name='delete_category'),
    
    path('enquiries/', views.enquiry_list, name='enquiry_list'),
    path('enquiries/update/<int:id>/', views.update_enquiry, name='update_enquiry'),
    path('enquiries/export/', views.export_enquiries_pdf, name='export_enquiries_pdf'),
    
    path('enquiries/customer/<str:mobile_number>/', views.customer_history, name='customer_history'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)