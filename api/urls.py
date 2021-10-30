from django.urls import path
from . import views

urlpatterns = [
    path('', views.apis, name='apis'),
    path('stud-list/', views.studentList, name='stud-lis'),
    path('stud-create/', views.studentCreate, name='stud-create'),
    path('stud-update/<int:pk>/', views.studentUpdate, name='stud-update'),
    path('stud-delete/<int:pk>/', views.studentDelete, name='stud-delete'),
]
