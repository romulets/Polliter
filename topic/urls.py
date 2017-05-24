from django.conf.urls import url
from django.contrib.auth import views as auth_views
import views

urlpatterns = [
    url(r'^$', views.list_topics, name='topic.list'),
    url(r'^votes/approve/(?P<id>[0-9]+)/$', views.approve_topic, name='topic.vote.approve'),
    url(r'^votes/disapprove/(?P<id>[0-9]+)/$', views.disapprove_topic, name='topic.vote.disapprove'),
    url(r'^votes/remove/(?P<id>[0-9]+)/$', views.remove_vote_on_topic, name='topic.vote.remove'),
]
