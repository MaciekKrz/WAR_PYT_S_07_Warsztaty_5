"""django_war5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from twitter.views import BaseView, MainPageView, AddTwitterView, AddUserView, LoginUserView, UserView

urlpatterns = [

    path('admin/', admin.site.urls),
    url(r'^$', BaseView.as_view(), name="index"),
    url(r'^main_page/$', MainPageView.as_view(), name="main"),
    url(r'^add_tweet/$', AddTwitterView.as_view(), name="add_tweet"),
    url(r'^add_user/$', AddUserView.as_view(), name="add_user"),
    url(r'^login/$', LoginUserView.as_view(), name="login"),
    url(r'^logout/$', LoginUserView.as_view(), name="logout"),
    url(r'^user/(?P<user_id>(\d)+)$', UserView.as_view(), name="user"),

]
