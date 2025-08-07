from django.urls import path
from . import views
urlpatterns = [

    path('register/', views.create_user, name='register'),
    path('login/', views.authenticate_user, name='authenticate'),
]
