from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("save/",views.register,name="saving"),
    path("show/",views.showid,name="show"),
    path("edit/",views.edit,name="edit"),
    path("changed/",views.change,name="change"),
    path("delete/",views.del_user,name="delete"),
]