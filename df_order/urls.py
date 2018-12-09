from django.conf.urls import url,include
import views
urlpatterns = [
    url('^$',views.order),
    url(r'^order_handle/$',views.order_handle),

]