from django.urls import path

from . import views

app_name = 'authentication'
urlpatterns = [
		path('', views.home, name='home'),
		path('signup/', views.signup, name='signup'),
		path('signin/', views.signin, name='signin'),
		path('signout/', views.logout, name='logout'),
]



