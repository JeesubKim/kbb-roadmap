from django.urls import path
from django.urls import include


from . import views

app_name = 'notification'
urlpatterns = [
    
    path('', views.main, name="main"),
    # path('create/', views.new_roadmap, name="create"),
    path('<str:id>/read/', views.is_read, name="is_read")
]
