from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('tasks.urls')),
    url(r'^new-data/', include('new_data.urls')),
]
