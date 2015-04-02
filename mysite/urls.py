from django.conf.urls import patterns, include, url
from django.contrib import admin
from wisertogether import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^data_sets/$', views.DataSetList.as_view()),
    url(r'^data_sets/(?P<pk>[0-9]+)/$', views.DataSetDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
