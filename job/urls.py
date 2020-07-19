from django.urls import path
from . import views
from . import api

app_name = 'job'
urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('add', views.add_job, name='add_job'),
    path('<int:slug>/', views.job_details, name='job_details'),

    # api 
    path('api/list' , api.job_list_api , name='job_list_api'),



]
