from django.urls import path, include
from register import views as v
from . import views


urlpatterns = [
path("<int:id>", views.index, name="index"),
path("", views.home, name="home"),
path('home/', views.home, name='home'),
path("register/", v.register, name="register"),
path('', include("django.contrib.auth.urls")),
]