from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from .forms import PostForm

# Create your views here.


def post_list(request):
    '''
    Read(R)
    포스트들을 불러와서 리스트 형태로 보여준다.
    '''
    posts = Post.objects.all()
    for post in posts:
        print(post)
    ctx = {'posts': posts}

    return render(request, template_name='posts/list.html', context=ctx)


def post_detail(request, pk):
    '''
    Read(R)
    특정 포스트를 불러와서 상세 정보를 보여준다.
    '''
    post = Post.objects.get(id=pk)
    ctx = {'post': post}

    return render(request, template_name='posts/detail.html', context=ctx)


def create_post(request):
    '''
    Create(C)
    포스트를 새로 생성한다
    request method ==> GET(url입력), POST(저장하기), PUT, DELETE
    '''
    if request.method == 'POST':
        # 글쓰기 칸을 '저장하기' 눌렀을때
        form = PostForm(request.POST)
        if form.is_valid():   # 형태 검정
            post = form.save()
            return redirect('posts:list')
    else:  # GET 방식
        # 글쓰기 칸을 보여주는 곳
        form = PostForm()
        ctx = {'form': form}

        return render(request, template_name='posts/post_form.html', context=ctx)


def update_post(request, pk):
    '''
    포스트를 수정하는 뷰
    '''
    post = get_object_or_404(Post, id=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()

            return redirect('posts:detail', pk)
        else:
            form = PostForm(instance=post)
            ctx = {'form': form}
            return render(request, 'posts/post_form.html', ctx)
