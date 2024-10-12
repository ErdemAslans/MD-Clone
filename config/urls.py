"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include 
from page.views import home_view
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', home_view, name= 'home_view'),
    path('blog/',include('Blog.urls',namespace ='blog')),
    path('user/', include('user_profile.urls', namespace='user')),
    path('admin/', admin.site.urls),
    path('read/',include('read.urls',namespace='read')),
    path('suport/', include('suport.urls', namespace='suport')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  