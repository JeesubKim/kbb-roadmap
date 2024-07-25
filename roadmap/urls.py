from django.urls import path
from django.urls import include


from . import views

app_name = 'roadmap'
urlpatterns = [
    
    path('', views.main, name="main"),
    path('create/', views.new_roadmap, name="create"),
    
]
