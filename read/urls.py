from django.urls import path
from .views import user_post_view,post_view_details

app_name = 'read'

urlpatterns = [
    path('<slug:user_slug>/',user_post_view,name='user_post_view'),
    path('<slug:user_slug>/<slug:post_slug>',post_view_details,name='post_view_details')
]
