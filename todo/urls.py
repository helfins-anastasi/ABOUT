from django.conf.urls import url
import todo.views as views

urlpatterns = [
    url(r'^$', views.todo_list, name="todo"),
    url(r'^(?P<pk>[0-9]+)$', views.detail, name="todo_detail"),
]
