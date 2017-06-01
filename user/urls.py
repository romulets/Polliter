from django.conf.urls import url
from django.contrib.auth import views as auth_views
import views

urlpatterns = [
    url(r'^$', auth_views.login, {
            'template_name': 'user/templates/login.html'
        }, name='user.login'),

    url(r'^logout$', auth_views.logout, {
      'next_page': 'user.login'
    }, name='user.logout'),

    url(r'^register$', views.register, name='user.register'),
    url(r'^home', views.home, name='user.home'),
]
