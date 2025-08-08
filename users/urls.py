from django.urls import path
from . import views
urlpatterns = [
    
    path('register/', views.create_user, name='register'),
    path('login/', views.authenticate_user, name='authenticate'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.view_update_user_profile, name='profile'),
]
