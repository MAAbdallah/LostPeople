from django.conf.urls import url
from . import views

app_name = 'LostPeople'


urlpatterns = [

    url(r'^$', views.ShowMissed, name="list"),
    url(r'^wating$', views.ShowWating, name="wait"),
    url(r'^create/$', views.missed_create, name="create"),
    url(r'^search/$', views.Search, name="search"),
    url(r'^filter/$', views.Search, name="filter"),
    url(r'^(?P<id>[0-9]+)/$', views.missed_detail, name="detail"),
    url(r'^(?P<id2>[0-9]+)/acc/$', views.accept, name="accept"),
    #url(r'^section/$', views.GetSection, name="home"),
    url(r'^child/$', views.Child, name="child"),
    url(r'^adult/$', views.Adult, name="adult"),
    url(r'^API/$', views.api, name="API"),
    url(r'^(?P<id3>[0-9]+)/Com/$', views.Make_comment, name="Comment"),
    url(r'^(?P<id4>[0-9]+)/deleteData/$', views.DeleteData, name="deleteData"),
    url(r'^(?P<id4>[0-9]+)/deleteWating/$', views.DeleteWating, name="deleteWating"),
]