"""GP2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url , include
from django.contrib import admin
#from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from LostPeople import views as missed_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^missed/', include('LostPeople.urls')),
    url(r'^services/', include('Products.urls')),

    url(r'^signup/$', missed_views.signup_view, name="signup"),
    url(r'^login/$', missed_views.login_view, name="login"),
    url(r'^logout/$', missed_views.logout_view, name="logout"),
    #url(r'^$', missed_views.ShowMissed, name="home"),
    url(r'^$', missed_views.GetSection, name="home"),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
