from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.home, name = 'searches_home'),
    url('^images$', views.music, name = 'searches_images'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^location/', views.search_location, name='search_location'),
    url(r'^tropics/', views.tropics, name='search_tropics'),
    url(r'^image/(\d+)',views.image,name ='search-id'),
    url(r'^image/(\d+)',views.images,name ='search-location')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)