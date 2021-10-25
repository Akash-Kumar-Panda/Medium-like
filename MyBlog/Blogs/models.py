from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# from Users.models import User
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=CASCADE)
    thumbNail = models.ImageField(default = '1.jpg',blank = True)

    # def __str__(self):
    #     return self.title