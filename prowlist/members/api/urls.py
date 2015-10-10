from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^quick-signup/', views.quick_signup, name='quick-signup'),
	url(r'^me/', views.me, name='user-information'),
]