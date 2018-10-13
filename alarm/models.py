from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class player(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    group = models.CharField(max_length = 10)
    player = models.CharField(max_length = 10)