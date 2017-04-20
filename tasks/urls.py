from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^subject/$', views.subject, name= "subject"),
    url(r'^new-task/$', views.new_task, name="new-task"),
    url(r'^new-subject/$', views.new_subject, name='new-subject'),
    url(r'^new-variant/$', views.new_variant, name='new-variant'),
]
