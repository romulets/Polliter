from django.conf.urls import url
from django.contrib.auth import views as auth_views
import views

urlpatterns = [
    url(r'^follow/(?P<id>[0-9]+)/$', views.follow_theme, name='theme.follow'),
    url(r'^unfollow/(?P<id>[0-9]+)/$', views.unfollow_theme, name='theme.unfollow'),
]
