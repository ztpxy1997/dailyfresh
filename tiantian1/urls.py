"""tiantian1 URL Configuration

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
import df_goods.views as gviews
import df_user.views as uviews
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^$', uviews.login),
    url(r'^user/',include('df_user.urls')),
    url(r'^cart/',include('df_cart.urls')),
    url(r'^order/',include('df_order.urls')),
    url(r'^goods/',include('df_goods.urls')),
    url(r'^tinymce/',include('tinymce.urls')),
    url(r'^list(\d+)_(\d+)_(\d+)/$',gviews.list),
    url(r'^(\d+)/$',gviews.detail),

]


