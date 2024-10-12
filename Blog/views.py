from django.shortcuts import render,redirect,get_object_or_404
from .forms import PostModelForm
from .models import Post,Category,Tag
from django.contrib import messages
import json

def PostModelView(request):
        form = PostModelForm()
        if request.method == "POST":
                form = PostModelForm(request.POST or None, request.FILES or None)
                if form.is_valid():
                        f = form.save(commit=False)
                        f.user = request.user
                        f.save()
                        tags = json.loads(form.cleaned_data.get('tag'))
                        for item in tags:
                                item ,created = Tag.objects.get_or_create(title = item.get('value').lower())
                                item.is_active = True
                                item.save()
                                f.tag.add(item) 
                        messages.success(request,'Conguralitons!!')
                        return redirect('home_view')
                        # f.save()

        content = dict(form=form)
        return render(request,'blog/form.html',content)

def TagView(request,tag_slug):
        tag = Tag.get_object_or_404(Tag,slug=tag_slug)
        posts = Post.objects.filter(tag = tag)
        context = dict(
                posts = posts,
                tag = tag,
        )

        return render(request,'post_list.html',context)

def CategoryView(request, category_slug):
    category = get_object_or_404(Category.objects, slug=category_slug)
    posts = Post.objects.filter(category=category)
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'post_list.html', context)
        

                                                