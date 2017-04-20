from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^ajax/$', views.ajax_html, name='ajax-html')
]
