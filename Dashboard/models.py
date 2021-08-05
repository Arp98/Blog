from django.db import models
import datetime


class Posts(models.Model):
    Post_User = models.CharField(max_length=200)
    Post_name = models.CharField(max_length=500)
    Post_Tags = models.CharField(max_length=500)
    Post_Contents = models.CharField(max_length=1000)
    Post_Timestamps = models.DateTimeField(default=datetime.datetime.now)
