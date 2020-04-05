"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^page(\d)',views.page_view,name='page'),
    url(r'^person/(?P<name>\w+)/(?P<age>\d{1,2})',views.person_view),
    url(r'^birthday/(?P<year>\d{4})/(?P<month>\d{1,2})',views.birthday_view),
    url(r'^login',views.login_view),
    url(r'^index',views.index_view),
    url(r'^add',views.add_view),
    url(r'^test_if',views.test_if_view),
    url(r'^test_for',views.test_for),
    url(r'^music$',views.sports_index),
    url(r'^shebao$',views.shebao),
    url(r'^test_static',views.test_static),
    url(r'^music/',include('music.urls')),
    url(r'^sports/',include('sports.urls')),
    url(r'^book/',include('music.urls'))
]