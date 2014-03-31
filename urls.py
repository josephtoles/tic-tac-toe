from django.conf.urls.defaults import patterns, include, url
from game import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.home),
	url(r'^select-player/', views.select_player),
	url(r'^new-game/', views.new_game),
	url(r'^move/', views.move),
)
