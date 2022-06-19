from django.conf.urls import url

from userapp import views

urlpatterns = [
    url(r'^login', views.login_user, name='login_user'),
]