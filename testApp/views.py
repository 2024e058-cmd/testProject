from django.shortcuts import render, redirect
from .forms import PostForm

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # 一覧ページへ
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})


from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


from django.shortcuts import render
def home(request): 
    return render(request, 'home.html')

        