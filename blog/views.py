from django.shortcuts import render
from .models import Post

# Create your views here.
def blog(request):

    context = {
        'posts' : Post.objects.all(),
    }

    return render(request, 'blog/posts.html', context)

def post(request, post_id):

    post = Post.objects.filter(id__icontains=post_id).first()

    context = {
        "post": post,
    }

    return render(request, 'blog/post.html', context)
