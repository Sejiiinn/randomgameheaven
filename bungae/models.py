from django.db import models
import datetime
#from login.models import user

# Create your models here.


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=50, unique=True)
    user_pw = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)

    class Meta:
        db_table = 'user'
        app_label = 'bungae'
        managed = False


class BungaeBoard(models.Model):
    bungae_num = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField(null=True)
    cre_date = models.DateTimeField(null=True)
    title = models.CharField(max_length = 50, null = True)
    post_title = models.CharField(max_length = 50, null = True)

    class Meta:
        db_table = 'bungaeboard'
        #app_label = 'bungae'
        managed = False