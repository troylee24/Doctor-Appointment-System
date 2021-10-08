from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root),
    path('doctors/', views.DoctorList.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', views.DoctorDetail.as_view(), name='doctor-detail'),
    path('patients/', views.PatientList.as_view(), name='patient-list'),
    path('patients/<int:pk>/', views.PatientDetail.as_view(), name='patient-detail'),
    path('appointments/', views.AppointmentList.as_view(), name='appointment-list'),
    path('appointments/<int:pk>/', views.AppointmentDetail.as_view(), name='appointment-detail'),
]