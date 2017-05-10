from django.conf.urls import url
from django.contrib.auth import views as auth_views
import views

urlpatterns = [
    url(r'^$', auth_views.login, {
            'template_name': 'templates/login.html'
        }, name='auth.login'),

    url(r'^logout$', auth_views.logout, {
      'next_page': 'auth.login'
    }, name='auth.logout'),

    url(r'^register$', views.register, name='register'),
]
