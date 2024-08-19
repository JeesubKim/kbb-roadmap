from django.urls import path

from . import views
app_name='user'


urlpatterns = [
    path('', views.main, name="main"),
    path('logout/', views.logout, name='logout'), 
    path('byname/', views.get_user_by_name, name='get_user_by_name'),
]
