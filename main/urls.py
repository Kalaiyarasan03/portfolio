from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('education/', views.education, name='education'),
    path('experience/', views.experience, name='experience'),
    path('certifications/', views.certifications, name='certifications'),
    path('contact/', views.contact, name='contact'),
    path('send-email/', views.send_email, name='send_email'),
]
