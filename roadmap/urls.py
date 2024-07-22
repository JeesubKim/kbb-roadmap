from django.urls import path
from django.urls import include


from . import views

urlpatterns = [
    
    path('', views.main, name="roadmap"),
    path('create/', views.new_roadmap, name="roadmap.create"),
    
]
