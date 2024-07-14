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
    path('admin/', admin.site.urls),

    path('user/', include('user.urls')),
    path('user/', include("allauth.urls")),
    
    # path('history/', include('history/urls')),
    # path('affiliate/', include('affiliate/urls')),
    # path('roadmap/', include('roadmap/urls')),
    # path('org/', include('org/urls')),
    # path('report/', include('report/urls')),
    # path('donation/', include('donation/urls')),

] 
