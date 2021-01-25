from django.urls import path
from django.urls import include
import blog.views

urlpatterns = [
    path('hello_world', blog.views.hello_world)
]
