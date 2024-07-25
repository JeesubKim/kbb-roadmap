"""
URL configuration for kbb_roadmap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('landing.urls')),
    path('history/', include('history.urls', namespace='history')),
    path('affiliate/', include('affiliate.urls', namespace='affiliate')),
    path('org/', include('org.urls', namespace='org')),
    path('roadmap/', include('roadmap.urls', namespace='roadmap')),
    path('event/', include('event.urls', namespace='event')),

    path('admin/', admin.site.urls),

    path('user/', include('user.urls', namespace='user')),
    path('donation/', include('donation.urls', namespace='donation')),
    path('user/', include("allauth.urls")),
    
    
    # path('report/', include('report.urls')),

] 
