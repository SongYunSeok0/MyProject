from django.shortcuts import render, redirect
from .models import Post, Category
from .forms import PostForm
from django.db.models import Q

# Create your views here.

def main(request):
    posts = Post.objects.all().order_by('-pk')
    categories = Category.objects.all()
    type_choices = Post._meta.get_field('type').choices
    return render(request, template_name='sh_shop/main.html', context={'posts':posts,
                                                                     'categories':categories,
                                                                     'type_choices': type_choices,})

def mypage(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    type_choices = Post._meta.get_field('type').choices
    return render(request, template_name='sh_shop/mypage.html', context={'posts':posts
                                                                      ,'categories':categories,
                                                                      'type_choices': type_choices,})

def category(request, slug):
    categories = Category.objects.all()
    type_choices = Post._meta.get_field('type').choices
    if slug =='no_category':
        # 미분류인 경우
        posts = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        posts = Post.objects.filter(category=category)
    return render(request, template_name='sh_shop/main.html',context={'posts':posts,
                                                                    'categories':categories,
                                                                    'type_choices': type_choices,})

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    categories = Category.objects.all()
    type_choices = Post._meta.get_field('type').choices
    return render(request, template_name='sh_shop/detail.html', context={'post':post
                                                                      ,'categories':categories,
                                                                      'type_choices': type_choices,})

def male(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    type_choices = Post._meta.get_field('type').choices
    return render(request, template_name='sh_shop/male.html', context={'posts':posts
                                                                      ,'categories':categories,
                                                                      'type_choices': type_choices,})

def female(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    type_choices = Post._meta.get_field('type').choices
    return render(request, template_name='sh_shop/female.html', context={'posts':posts
                                                                      ,'categories':categories,
                                                                      'type_choices': type_choices,})

def gender_filter(request, gender):
    categories = Category.objects.all()
    posts = Post.objects.filter(gender=gender).order_by('-pk')
    type_choices = Post._meta.get_field('type').choices
    return render(request, 'sh_shop/main.html', {
        'posts': posts,
        'categories': categories,
        'type_choices': type_choices,
    })

def gender_type_filter(request, gender, type):
    categories = Category.objects.all()
    posts = Post.objects.filter(gender=gender, type=type).order_by('-pk')
    type_choices = Post._meta.get_field('type').choices
    return render(request, 'sh_shop/main.html', {
        'posts': posts,
        'categories': categories,
        'type_choices': type_choices,
    })


def search(request):
    query = request.GET.get('q', '')
    categories = Category.objects.all()
    type_choices = Post._meta.get_field('type').choices

    if query:
        posts = Post.objects.filter(
            Q(type__icontains=query) |
            Q(gender__icontains=query) |
            Q(brand__icontains=query) |
            Q(price__icontains=query) |
            Q(size__icontains=query) |
            Q(content__icontains=query)
        ).order_by('-pk')
    else:
        posts = Post.objects.none()  # 검색어 없으면 결과 없음

    return render(request, 'sh_shop/search.html', {
        'query': query,
        'posts': posts,
        'categories': categories,
        'type_choices': type_choices,
    })

def create(request):
    categories = Category.objects.all()
    type_choices = Post._meta.get_field('type').choices
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
                           'categories':categories,
                           'type_choices': type_choices,})