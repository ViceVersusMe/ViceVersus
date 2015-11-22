from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^vice/', include('vice.urls')),
    url(r'^user/', include('users.urls')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^admin/', include(admin.site.urls)),
]
