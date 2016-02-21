from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<detail_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^roll/$', views.roll, name='roll'),
]