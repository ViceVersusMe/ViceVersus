from django.conf.urls import url


urlpatterns = [

    url(r'^', 'vice.views.home', name='home'),
]
