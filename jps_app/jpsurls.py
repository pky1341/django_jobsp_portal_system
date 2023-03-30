from django.urls import path
from jps_app import views

urlpatterns=[
    path('',views.index,name='index'),
    path('/find_job',views.find_job,name="find_job")
]