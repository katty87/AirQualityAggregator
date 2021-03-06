from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^service/(?P<service_id>[0-9]+)/(?P<station_id>[0-9]+)/(?P<substance_id>[0-9]+)$',
        views.SubstanceDetailView.as_view(), name='substance-detail'),
    url(r'^service/service/(?P<substance_id>[0-9]+)$', views.SubstanceServicesDetailView.as_view(),
        name='substance-det-services'),
    url(r'^service/station/(?P<substance_id>[0-9]+)$', views.SubstanceStationsDetailView.as_view(),
        name='substance-det-stations'),
]
