from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.posts_list, name="list"),
    path('post-new/', views.post_new, name="post-new"),
    path('update/<slug:slug>', views.update_post, name="update"),
    path('delete/<slug:slug>', views.delete_post, name="delete"),
    path('comment/<slug:slug>', views.create_comment, name="comment"),
    path('categories/', views.categories_list, name="categories"),
    path('category/<int:cat_id>', views.category, name="category"),
    path('<slug:slug>', views.post_page, name="page"),
]