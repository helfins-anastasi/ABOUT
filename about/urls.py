from django.conf.urls import include, url
from django.contrib import admin
import todo.views as views
import todo.urls
import social_django.urls
import django.contrib.auth.urls

admin.autodiscover()

urlpatterns = [
    url(r'^secret-login-form/$', views.user_login, name='secret_login'),
    url(r'^login$', views.login, name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.todo_list, name="list"),
    url(r'^suggest', views.suggest, name="suggest"),
    url(r'^item/', include(todo.urls)),
    url('', include(social_django.urls, namespace="social")),
    url('', include(django.contrib.auth.urls, namespace='auth')),
]
