from django.db import models

class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=50)
    user_pw = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, unique=True)
    
class Board(models.Model):
    board_num = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
    cre_date = models.DateTimeField(auto_now_add=True)
    board_type = models.CharField(max_length=50)