from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users/create_client_user/$', views.create_client_user, name='create-user'),
]