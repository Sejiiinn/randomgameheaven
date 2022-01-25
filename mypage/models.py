from django.db import models

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