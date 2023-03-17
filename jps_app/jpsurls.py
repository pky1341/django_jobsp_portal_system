from django.urls import path
from jps_app import views

urlpatterns=[
    path('',views.index,name='index')
]