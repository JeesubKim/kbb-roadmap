from django.urls import path
from django.urls import include


from . import views
app_name='user'
urlpatterns = [
    
    path('', views.main, name="main"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name='logout'), 
    # path("user/", )
]
