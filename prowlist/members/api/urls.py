from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^quick-signup/', views.quick_signup, name='quick-signup'),
	url(r'^me/', views.me, name='member-information'),
	url(r'^update/', views.enhance_user, name='enhance-member'),
]