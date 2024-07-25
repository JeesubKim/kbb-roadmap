from django.urls import path
from django.urls import include


from . import views
app_name="history"
urlpatterns = [
    
    path('', views.main, name="main"),
    
]
