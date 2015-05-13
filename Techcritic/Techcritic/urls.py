from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'search/', 'Techcritic.views.search'), #url for results page of search
    url(r'update_likes/', 'Techcritic.views.update_likes'), 

    url(r'^$', 'Techcritic.views.index', name='home'),
]
