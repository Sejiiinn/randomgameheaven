from tkinter import CASCADE
from django.db import models
from django.forms import ImageField
from wordcloud import ImageColorGenerator

class user(models.Model):
    user_id = models.CharField(primary_key=True, max_length=50)
    user_pw = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, unique=True)
    
    class Meta:
        db_table = 'user'
        app_label = 'mypage'
        managed = False
    
class board(models.Model):
    board_num = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    title = models.TextField(null = True)
    content = models.TextField(null = True)
    cre_date = models.DateTimeField(null = True)
    board_type = models.CharField(max_length=50, null = True)

    class Meta:
        db_table = 'board'
        app_label = 'mypage'
        managed = False

        
class Usergame(models.Model):
    user_game_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(user, on_delete=CASCADE, max_length=50)
    user_game_title = models.CharField(max_length=50)
    user_game_content = models.TextField()
    user_game_img = ImageField()
    date_time = models.DateTimeField()
    
    class Meta:
        db_table = 'user_game'
        app_label = 'mypage'
        managed = False