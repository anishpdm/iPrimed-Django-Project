
from django.urls import path, include
from . import views

urlpatterns = [

    path('add/', views.studentAddPage, name='studentAddPage'),
    path('addnumbers/', views.addNumbers, name='addNumbers'),
 

]
