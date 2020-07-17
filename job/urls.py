from django.urls import path
from . import views

app_name = 'job'
urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('<int:job_id>/', views.job_details, name='job_details'),
]
