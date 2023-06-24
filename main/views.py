from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from .models import Post
import markdown
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

def index(request):
    return render(request, 'main/index.html')

def blog(request):
    postlist = Post.objects.all()
    return render(request, 'main/blog.html', {'postlist': postlist})

def posting(request, pk):
    post = Post.objects.get(pk=pk)
    md = markdown.Markdown(extensions=['fenced_code', 'codehilite'])
    content_html = md.convert(post.contents)
    return render(request, 'main/posting.html', {'post': post, 'content_html': content_html})

def new_post(request):
    if request.method == 'POST':

        # 추가된 코드 :
        if 'mainphoto' in request.FILES:
            mainphoto = request.FILES['mainphoto']
            mainphoto_name = default_storage.save(mainphoto.name, mainphoto)
        else:
            mainphoto_name = None  # mainphoto가 없으면 None으로 설정

        new_article = Post.objects.create(
            postname=request.POST['postname'],
            contents=request.POST['contents'],
            kindcode=request.POST['kindcode'],
            mainphoto=mainphoto_name,
        )

        return redirect('/blog/')
    return render(request, 'main/new_post.html')

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', {'Post': post})

