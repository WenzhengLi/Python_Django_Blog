from django.urls import path
from django.urls import include
import blog.views

urlpatterns = [
    path('hello_world', blog.views.hello_world),
    path('blog_page', blog.views.article_content),
    path('index', blog.views.get_index_page),
    path('detail/<int:article_id>', blog.views.get_detail_page)
]
