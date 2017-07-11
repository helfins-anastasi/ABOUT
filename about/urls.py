from django.conf.urls import include, url
from django.contrib import admin
import hello.views
import todo.views
import todo.urls
import social_django.urls
import django.contrib.auth.urls

admin.autodiscover()

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^secret-login-form/$', todo.views.user_login, name='secret_login'),
    url(r'^login$', todo.views.login, name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^list/', include(todo.urls)),
    url('', include(social_django.urls, namespace="social")),
    url('', include(django.contrib.auth.urls, namespace='auth')),
]
