from django.db import models
class user(models.Model):
    user_id = models.CharField(max_length=50, unique=True)
    user_pw = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
# Create your models here.
