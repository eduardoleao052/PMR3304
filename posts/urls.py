from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.posts_list, name="list"),
    path('post-new/', views.post_new, name="post-new"),
    path('<slug:slug>', views.post_page, name="page")
]