from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=100)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    creation_date = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(User, related_name='votes', blank=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def count_upvotes(self):
        return self.upvotes.count()

    @property
    def name_of_author(self):
        return self.author.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments_creator")
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comments: {self.post.id}'

    @property
    def name_of_author(self):
        return self.author.name