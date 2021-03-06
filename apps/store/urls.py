"""project_catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_products, name='store_list_products'),
    url(r'^create', views.create, name='store_create_product'),
    url(r'^edit/(?P<product_id>\d+)/$', views.edit, name='store_edit_product'),
    url(r'^update/(?P<product_id>\d+)/$', views.update, name='store_update_product'),
    url(r'^add_cart/$', views.add_cart, name='store_add_cart'),
    url(r'^delete_cart/(?P<cart_id>\d+)/$', views.delete_cart, name='store_delete_cart'),
    url(r'^checkout$', views.checkout, name='store_checkout'),
    url(r'^commit_order', views.commit_order, name='store_commit_order'),

    # url(r'^products/', include('apps.store.urls')),
    # url(r'^admin/', admin.site.urls),
]
