from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', auth_views.login, {
            'template_name': 'templates/login.html'
        }, name='login'),

    url(r'^logout$', auth_views.logout, name='logout'),
    # url(r'^register$', views.register, name='register'),
]
