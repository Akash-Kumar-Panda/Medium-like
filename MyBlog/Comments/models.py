from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from Blogs.models import Blog

# Create your models here.

class Comment(models.Model):
    content = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=CASCADE)
    blog = models.ForeignKey(Blog,on_delete=CASCADE)
