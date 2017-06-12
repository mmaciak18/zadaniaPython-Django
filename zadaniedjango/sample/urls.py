from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.list_of_users, name='list_of_users'),
    url(r'^edit/', views.edit, name="edit"),
    url(r'^view/', views.view, name="view"),
    url(r'^delete/', views.delete, name="delete"),
    url(r'^add/', views.add, name="add"),
    url(r'^csvview/', views.csvview, name="csvview"),
]
