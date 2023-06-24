from django.db import models

# Create your models here.
#게시글(Post) -> 제목(postname), 내용(contents) 필요!!
class Post(models.Model):
  postname = models.CharField(max_length=50)
  contents = models.TextField()
