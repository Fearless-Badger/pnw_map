from django.urls import path
from .views import EventListCreateView, StudentListCreateView, RegistrationListCreateView
from . import views

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('registrations/', RegistrationListCreateView.as_view(), name='registration-list-create'),
    path('register/', views.register_student, name='register_student'),
    path('login/', views.login_student, name='login_student'),
]