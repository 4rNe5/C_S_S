from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'main/index.html')

# blog.html 페이지를 부르는 blog 함수
def blog(request):
    return render(request, 'main/blog.html')
