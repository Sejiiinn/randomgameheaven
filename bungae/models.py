from operator import mod
from pyexpat import model
from django.db import models
import datetime
from login.models import user

# Create your models here.



class BungaeBoard(models.Model):
    bungae_num = models.AutoField(primary_key=True)
    User = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    content = models.TextField(null=True)
    cre_date = models.DateTimeField(null=True)
    title = models.CharField(max_length = 50, null = True)
    post_title = models.CharField(max_length = 50, null = True)

    class Meta:
        db_table = 'bungaeboard'
        #app_label = 'bungae'
        managed = False