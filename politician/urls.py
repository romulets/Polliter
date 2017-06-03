from django.conf.urls import url
from django.contrib.auth import views as auth_views
import views

urlpatterns = [
    url(r'^$', views.home, name='politician.home'),
    url(r'^list$', views.list_politicians, name='politician.list'),
    url(r'^follow/(?P<id>[0-9]+)/$', views.follow_politician, name='politician.follow'),
    url(r'^unfollow/(?P<id>[0-9]+)/$', views.unfollow_politician, name='politician.unfollow'),
]
