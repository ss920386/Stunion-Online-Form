from django.conf.urls import url
from reflect.views import *

urlpatterns = [
	#url(r'^$',ReflectionDetailView.as_view(), name="list"),
    url(r'^$', ReflectionListView.as_view(), name='list'),
    url(r'^important/$', ReflectionListViewImportant.as_view(), name='important'),
    url(r'^(?P<pk>\d+)/$',ReflectionDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/delete/$',ReflectDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/mark/$',markImportant, name='mark'),
]