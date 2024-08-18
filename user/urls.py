from django.urls import path
from django.urls import include
from rest_framework import routers

from . import views
app_name='user'

# router = routers.DefaultRouter()
# router.register(r'byname', views.UserViewSet)

urlpatterns = [
    
    path('', views.main, name="main"),
    # path('login/', views.login, name="login"),
    path('logout/', views.logout, name='logout'), 
    path('byname/', views.get_user_by_name, name='get_user_by_name'),

    
    # path("user/", )
]
