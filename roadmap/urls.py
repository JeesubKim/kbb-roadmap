from django.urls import path
from django.urls import include


from . import views

app_name = 'roadmap'
urlpatterns = [
    
    path('', views.main, name="main"),
    path('detail/<str:id>/', views.detail, name="detail"),
    path('create/', views.new_roadmap, name="create"),

    # path('detail/comment/likes/<str:id>/', views.likes, name="likes"),
    path('detail/<str:id>/agreement/<str:type>/', views.agree, name="agree"),
    path('detail/<str:id>/complete/', views.complete, name="complete")
]
