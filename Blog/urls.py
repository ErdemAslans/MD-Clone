from django.urls import path
from .views import PostModelView,CategoryView,TagView

app_name = 'Blog'

urlpatterns = [
    path('create/',PostModelView, name= 'PostModelView'),
    path('category/<slug:category_slug>/',CategoryView,name = 'CategoryView'),
    path('tag/<slug:tag_slug>/',TagView,name='TagView'),
]