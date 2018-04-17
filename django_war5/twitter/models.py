from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    content = models.CharField(max_length=64)
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=None)
