from django.contrib import admin
from django.urls import path , include
from . import views 
from planner_app import views 

urlpatterns = [
    
    path('' , views.home, name="home"),
    
    path('index', views.index, name='index'),
    path('index_open', views.index_open, name='index_open'),
    
    # path('admin/', admin.site.urls),
    path('all_events/', views.all_events, name='all_events'), 
    path('add_event/', views.add_event, name='add_event'), 
    path('update/', views.update, name='update'),
    path('remove/', views.remove, name='remove'),
] 