from django.conf.urls import url
from beers.views import first_view, beer_list_view, beer_detail_view, all_beers_list_view


urlpatterns = [
    url(r'^$', first_view, name='first-view'),
    url(r'^list/$', beer_list_view, name='beer-list-view'),
    url(r'^cuentos/$', all_beers_list_view, name='all-beers-list-view'),
    url(r'^detail/(?P<id>\d+)/$', beer_detail_view, name='beer-detail-view'),
]