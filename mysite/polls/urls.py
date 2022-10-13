from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path('', views.index, name='index'),
    path("user/", views.userlist2, name="user"),
    path('<int:id>/', views.address, name="address"),
    path('<int:id>/results/', views.results, name="results"),
    path('<int:id>/vote', views.vote2, name="vote"),
    path('userlist', views.userlist, name="userlist")

]
