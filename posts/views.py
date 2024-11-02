from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Categories, PostInCategory
from django.contrib.auth.decorators import login_required
from . import forms
from .forms import CommentForm

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})

@login_required(login_url="/users/login")
def secret_post(request):
    post = Post.objects.get(slug='secret-post')
    return render(request, 'posts/post_page.html', {'post':post})

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    post_id = post.id
    cat_id = PostInCategory.objects.filter(post=post_id).values_list('cat')[0][0]
    cat = Categories.objects.get(pk=cat_id)
    comments = Comment.objects.filter(post=post_id).order_by('-date')
    return render(request, 'posts/post_page.html', {'post': post, 'cat': cat, 'comments': comments})

@login_required(login_url="/users/login")
def post_new(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.slug = int(Post.objects.values_list('slug').order_by('-slug')[0][0]) + 1
            new_post.save()
            return redirect("posts:list")
    else: 
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', {'form': form})

def update_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        post.title = request.POST['title']
        post.author = post.author
        post.date = post.date
        post.body = request.POST['body']
        post.save()
        return render(request, 'posts/post_page.html', {'post': post})

    return render(request, 'posts/update.html', {'post': post})


def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        post.delete()
        return redirect("posts:list")

    return render(request, 'posts/delete.html', {'post': post})

@login_required(login_url="/users/login")
def create_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post_id = post_id = post.id
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = request.user
            comment_body = form.cleaned_data['body']
            comment = Comment(author=comment_author,
                              body=comment_body,
                              post=post)
            comment.save()
            return render(request, 'posts/post_page.html', {'post': post})
    else:
        form = CommentForm()
    comments = Comment.objects.filter(post=post_id).order_by('-date')
    return render(request, 'posts/comment.html', {'form': form, 'post': post, 'comments': comments})

def categories_list(request):
    cats = Categories.objects.all()
    return render(request, 'posts/categories.html', {'cats': cats})


def category(request, cat_id):
    post_ids = PostInCategory.objects.filter(cat=cat_id).values_list('post')
    cat = Categories.objects.get(pk=cat_id)
    posts = []
    for id in post_ids:
        posts.append(Post.objects.filter(pk=id[0])[0])
    return render(request, 'posts/category.html', {'posts': posts, 'cat': cat})
    pass