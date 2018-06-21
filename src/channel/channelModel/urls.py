from django.conf.urls import url
from channelModel import views

urlpatterns = [
    url(r'^channels/$', views.channel_list),
    url(r'^channels/(?P<pk>[^/]+)/$', views.channel_detail),
]