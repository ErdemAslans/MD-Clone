from django.shortcuts import render,get_object_or_404
from user_profile.models import Profile
from Blog.models import Post

def user_post_view(request, user_slug):
    profile = get_object_or_404(Profile, slug=user_slug)
    posts = Post.objects.filter(user=profile.user, is_active=True)
    context = {
        'profile': profile,
        'posts': posts
    }
    return render(request, 'read/all_post.html', context)


def post_view_details(request,user_slug,post_slug):

    post = get_object_or_404(Post, slug=post_slug)  
    post.view_count += 1
    post.save()

    context= dict(
        post=post,
    )

    return render(request,'read/post_details.html',context)