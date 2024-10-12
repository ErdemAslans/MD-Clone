from django.shortcuts import render
from Blog.models import Post,Category,Tag

def home_view(request):
    posts = Post.objects.filter(is_active = True)
    categories = Category.objects.filter(is_active=True)
    tags = Tag.objects.filter(is_active=True)
    context = dict(
        posts = posts,
        categories = categories,
        tags = tags,
    )
    return render(request,'page/home_page.html',context)
