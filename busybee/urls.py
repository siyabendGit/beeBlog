from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from . import views
from busybee.views import business
from django.conf import settings
urlpatterns = [
    url(r'^$', views.busybee, name='busybee'),
    url(r'^business/$', business),
]
urlpatterns += staticfiles_urlpatterns()