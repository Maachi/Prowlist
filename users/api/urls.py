from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users/auth/device/$', views.authenticate_device, name='authenticate-device'),
]