from django.urls import path
from . import views
urlpatterns = [
     path('root/', views.root, name='root'),
    path('register/', views.create_user, name='register'),

]
