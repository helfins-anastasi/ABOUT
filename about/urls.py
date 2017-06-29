from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views
import todo.views

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^list/', todo.views.todo_list, name='todo'),
]
