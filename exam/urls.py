from django.urls import path

from.import views

urlpatterns = [
    path('', views.login),
    path('login',views.login,name="login"),
    path('index',views.index,name="index"),
    path('home',views.home,name="home"),
    path('schedule',views.schedule,name="schedule"),
    path('profile',views.profile,name="profile"),
    path('logout',views.logout,name="logout"),
    path('allocate',views.allocate,name="allocate"),
    ]