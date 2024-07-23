from . import views
from django.contrib import admin
from django.urls import path
app_name = 'fapp'

urlpatterns = [
   
    # path('demo/',views.demo,name='demo'),
    # path('',views.home,name='home'),
    path('',views.demo,name='demo'),
    path('demo/',views.home,name='home'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
    
]