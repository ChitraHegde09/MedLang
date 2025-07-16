from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('select/', views.select_symptoms, name='select_symptoms'),
    path('learn/', views.learn_view, name='learn'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
