from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    # url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', include('vice.urls')),
    url(r'^user/', include('users.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
