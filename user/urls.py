from django.urls import path
from django.urls import include


from . import views

urlpatterns = [
    
    path('', views.main, name="main"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name='logout'), # 코드 추가하기
    # path("user/", )
]
