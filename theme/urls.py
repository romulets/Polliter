from django.conf.urls import url
from django.contrib.auth import views as auth_views
import views

urlpatterns = [
    url(r'^follow$', views.follow_theme, name='theme.follow'),
    url(r'^unfollow$', views.unfollow_theme, name='theme.unfollow'),
]
