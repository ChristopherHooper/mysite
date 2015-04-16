from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^category/$', views.CatagoryView.as_view(), name='category'),
#     url(r'^category/(?P<first>)[0-9]+/events/$', views.events, name='events'),
	url(r'^category/events/$', views.events, name='events'),
    #url(r'^category/eventsview/(?P<favorites>)$', views.EventsView.as_view(), name='eventsview'),
    url(r'^category/eventsview/$', views.EventsView.as_view(), name='eventsview'),
    url(r'^category/error/$', views.Error.as_view(), name='error'),
]
