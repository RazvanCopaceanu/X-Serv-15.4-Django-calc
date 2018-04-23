from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'calc.views.barra'),
    url(r'^(-?\d+)/(.+)/(-?\d+)$', 'calc.views.calcular'),
    url(r'^admin/', include(admin.site.urls)),
]
