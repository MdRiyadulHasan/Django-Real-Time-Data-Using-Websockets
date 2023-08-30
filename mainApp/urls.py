from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home, name = 'home'),
    path('student/', views.generate_student_data, name = 'generate_student_data'),
]