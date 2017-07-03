from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views
import todo.views

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^list/(?P<username>[a-zA-Z0-9_-]+)$', todo.views.todo_list, name="todo"),
    url(r'^list/(?P<username>[a-zA-Z0-9_-]+)/(?P<pk>[0-9]+)$', todo.views.detail, name="todo_detail")
]
