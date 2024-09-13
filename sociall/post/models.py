from django.contrib.auth.models import User
from django.db import models
from account.models import Profile

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField(Profile, related_name='liked_posts', blank=True)
    comments = models.ManyToManyField(Profile, through='Comment', related_name='commented_posts', blank=True)

    def __str__(self):
        return self.title

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like_set')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_set')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
