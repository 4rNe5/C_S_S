from django.db import models

class Post(models.Model):
    postname = models.CharField(max_length=50)
    kindcode = models.CharField(max_length=50, null=True)
    mainphoto = models.ImageField(blank=True, null=True) # 
    contents = models.TextField()

    # postname이 Post object 대신 나오기
    def __str__(self):
        return self.postname
