from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^subject/$', views.subject, name= "subject"),
    url(r'^new-task/$', views.new_task, name="new-task"),
]
