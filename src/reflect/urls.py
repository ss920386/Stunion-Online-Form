from django.conf.urls import url
from reflect.views import ReflectionListView, ReflectionDetailView, ReflectDeleteView

urlpatterns = [
	#url(r'^$',ReflectionDetailView.as_view(), name="list"),
    url(r'^$', ReflectionListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$',ReflectionDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/delete/$',ReflectDeleteView.as_view(), name='delete')
]