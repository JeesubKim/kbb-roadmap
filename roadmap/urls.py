from django.urls import path
from django.urls import include


from . import views

app_name = 'roadmap'
urlpatterns = [
    
    path('', views.main, name="main"),
    path('detail/<str:id>/', views.detail, name="detail"),
    path('create/', views.new_roadmap, name="create"),
    
]
