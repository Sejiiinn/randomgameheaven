from django.db import models
from django.conf import settings # 이따 지워볼것
class user(models.Model):
    user_id = models.CharField(primary_key=True, max_length=50, unique=True)
    user_pw = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    class Meta:
        db_table = 'user'
        app_label = 'main'
        managed = True

# Create your models here.
