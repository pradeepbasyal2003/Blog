from django.urls import path , include
from .views import *

urlpatterns = [
    path("", Home, name= "home"),
    path("blog/<slug>" , Post_view , name="post_view"),
]
