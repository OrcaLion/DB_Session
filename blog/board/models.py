from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()

    def __str__(self):
        return self.content

class Comment(models.Model) :
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = "comments")
    content = models.TextField()