from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('table', views.table, name="table"),
    path('form', views.createTask, name="createTask"),
    path('logout', views.logout, name="logout"),
    path('page', views.page, name="page"),

]