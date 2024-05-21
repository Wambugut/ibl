from django.db import models

from django.utils import timezone


class subscribers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(default=timezone.now)
    banner=models.ImageField(default='fallback.png', blank='true')
def __str__(self):
    return self.email 