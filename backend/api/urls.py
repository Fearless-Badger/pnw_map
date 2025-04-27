from django.urls import path
from .views import EventListCreateView, StudentListCreateView, RegistrationListCreateView

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('registrations/', RegistrationListCreateView.as_view(), name='registration-list-create'),
]