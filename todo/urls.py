from django.conf.urls import url
import todo.views as views

urlpatterns = [
    url(r'^login$', views.login, name="login"),
    url(r'^(?P<username>[a-zA-Z0-9_-]+)$', views.todo_list, name="todo"),
    url(r'^(?P<username>[a-zA-Z0-9_-]+)/(?P<pk>[0-9]+)$', views.detail, name="todo_detail"),
]
