from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PostForm
from .models import Post


# Create your views here.
def index(request):
    # if the method is POST
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        
        # if the form is valid
        if form.is_valid():
        # Yes, Save
            form.save()
        
        # Redirect to Home
            return HttpResponseRedirect('/')

            
        else:
            # No, Show errors
            return HttpResponseRedirect(form.errors.as_json())

    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('created_at')[:20]
    

    # Show
    return render(request, 'posts.html', {'posts': posts})


def delete(request, post_id):
    # Find user
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')



