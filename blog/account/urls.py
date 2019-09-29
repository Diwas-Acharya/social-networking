from django.urls import include, path
from . import views


urlpatterns = [
    path('profile/<int:myid>',views.profile),
    path('userprofile/<int:userid>',views.userprofile),
    path('usernotifications/<int:userid>',views.usernotifications),
    path('userchat/<int:userid>',views.userchat),
    path('userprofile/<int:userid>',views.userprofile),
    path('friends/<int:userid>',views.userfriends),
    path('userdetailes/<int:friendid>/<int:userid>',views.userdetailes),
    path('register/<int:id>',views.register)
  ]
