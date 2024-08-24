from django.urls import path
from django.urls import include


from . import views
app_name="comments"
urlpatterns = [
    
    path('', views.main, name="main"),
    path('likes/<str:type>/<str:id>/', views.likes, name="likes")

    # const url = `/comment/likes/${comment_id}/`;
]
