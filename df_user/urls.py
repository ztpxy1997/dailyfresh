from django.conf.urls import url,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import views
urlpatterns = [
    url(r'^register/$',views.register),
    url(r'^register_handle/$',views.register_handle),
    url(r'^login/$',views.login),
    url(r'^login_hander/$',views.login_hander),
    url(r'^info/$',views.info),
    url(r'^order/$',views.order),
    url(r'^center_site/$',views.center_site),
    url(r'^loginout/$',views.loginout),
    url(r'^user_order_(\d)/$',views.user_centent_order),
]