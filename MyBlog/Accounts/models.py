from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class BloggerData(models.Model):
    done = 'verified'
    notDone = 'not verified'

    verificationStatus = [
        (done,'verified'),
        (notDone,'notVerified'),
    ]

    about = models.TextField()
    designation = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    status = models.CharField(max_length=15,choices = verificationStatus,default=notDone)
    user = models.OneToOneField(User,on_delete=CASCADE,primary_key=True )