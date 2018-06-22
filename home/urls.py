from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^single$', views.single, name='single'),
	url(r'^index$', views.post_list, name='index'),
	url(r'^gallery$', views.gallery, name='gallery'),
	url(r'^archive$', views.archive, name='archive'),
	url(r'^contact$', views.contact, name='contact'),
]