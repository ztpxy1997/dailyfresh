
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url,include
import views
urlpatterns = [
    url(r'^index/$',views.index),
]