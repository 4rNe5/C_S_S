from django.contrib import admin
from django.urls import path
from main.views import index, blog, posting

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog/<int:pk>/', posting, name="posting"),  # 주의! 슬래시(/)가 추가되어야 합니다.
]
