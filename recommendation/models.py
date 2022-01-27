from django.db import models
# from login.models import user

# Create your models here.

class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=50, unique=True)
    user_pw = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)

    class Meta:
        db_table = 'user'
        app_label = 'recommendation'
        managed = False




class Post(models.Model):
    user_game_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user_game_title = models.CharField(max_length=50)
    user_game_content = models.TextField()
    user_game_img = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_game'
        app_label = 'recommendation'
        managed = False
