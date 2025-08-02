from django.shortcuts import render, redirect
from .models import Post, Category
from .forms import PostForm
# Create your views here.

def main(request):
    posts = Post.objects.all().order_by('-pk')
    categories = Category.objects.all()
    return render(request, template_name='sh_shop/main.html', context={'posts':posts,
                                                                     'categories':categories})

def category(request, slug):
    categories = Category.objects.all()
    if slug =='no_category':
        # 미분류인 경우
        posts = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        posts = Post.objects.filter(category=category)
    return render(request, template_name='sh_shop/main.html',context={'posts':posts,
                                                                    'categories':categories})

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    categories = Category.objects.all()
    return render(request, template_name='sh_shop/detail.html', context={'post':post
                                                                      ,'categories':categories})

def create(request):
    categories = Category.objects.all()
    if request.method == "POST":
        # 제출 버튼을 누른경우
        postform = PostForm(request.POST, request.FILES)
        if postform.is_valid():
            # 정상값인 경우
            postform.save()
            return redirect('main')
    else: # get
        postform = PostForm()
    return render(request, template_name='sh_shop/postform.html',
                  context={'postform':postform,
                           'categories':categories})