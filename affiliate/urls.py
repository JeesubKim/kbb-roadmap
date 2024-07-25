from django.urls import path
from django.urls import include


from . import views
app_name="affiliate"
urlpatterns = [
    
    path('', views.main, name="main"),
    
]
