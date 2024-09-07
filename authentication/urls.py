# authentication/urls.py

from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.conf.urls.static import static
from django.conf import settings
from .views import child_details

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('all-users/', views.all_users, name='all_users'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('reset-password/<int:user_id>/', views.reset_password, name='reset_password'),
    path('edit-user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('register-child/', views.register_child, name='register_child'),
    path('all-children/', views.all_children_view, name='all_children'),
    path('child-details/<int:child_id>/', child_details, name='child_details'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
