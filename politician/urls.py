from django.conf.urls import url
from django.contrib.auth import views as auth_views
import views

urlpatterns = [
    url(r'^follow$', views.follow_politician, name='politician.follow'),
    url(r'^unfollow$', views.unfollow_politician, name='politician.unfollow'),
]
