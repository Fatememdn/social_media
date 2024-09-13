from django.urls import path
from .views import *

urlpatterns = [
    path("post-create/", Postcreate.as_view()),
    path("post-list/", PostList.as_view()), 

]