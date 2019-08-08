from django.conf.urls import url
from . import views

app_name = 'Products'


urlpatterns = [

    url(r'^Product/$', views.ShowProducts, name="listP"),
    url(r'^Generate/$', views.generateCharity, name="generateC"),
    url(r'^charity/$', views.ShowCharity, name="listC"),
    url(r'^createP/$', views.product_create, name="createP"),
    url(r'^createC/$', views.createCharity, name="createC"),
    url(r'^(?P<id>[0-9]+)/$', views.product_detail, name="detailP"),
    url(r'^(?P<id2>[0-9]+)/fav/$', views.BookMark, name="fav"),
    url(r'^Myfav/$', views.MyBookmark, name="Myfav"),
    url(r'^(?P<id3>[0-9]+)/deleteProduct/$', views.DeleteProduct, name="deleteProduct"),
    url(r'^(?P<id4>[0-9]+)/deleteCharity/$', views.DeleteCharity, name="deleteCharity"),

]