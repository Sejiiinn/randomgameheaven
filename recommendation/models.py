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
<<<<<<< HEAD
    user_game_content = models.TextField()
    user_game_img = models.ImageField(upload_to='images/')
    date_time = models.DateTimeField(auto_now_add=True)
=======
    user_game_content = models.CharField(max_length=300)
    user_game_img = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    # imgfile = models.ImageField(null=True, upload_to="", blank=True)
>>>>>>> 556881a43484d7b6c1a6d8f2fa7d482e005671b3

    class Meta:
        db_table = 'user_game'
        app_label = 'recommendation'
        managed = False


# class FileUpload(models.Model):
#     # title = models.TextField(max_length=40, null=True)
#     imgfile = models.ImageField(null=True, upload_to="", blank=True)
#     # content = models.TextField()